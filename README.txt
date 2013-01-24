Oveview
=======

Fast routine to seemlessly classify and store incoming data into an infinite number Protocol Buffer files (\"bins\"). Bins are grouped into directories by a specific field. Data can then be retrieved by the grouped-field's value. Virtually any data can be stored for fast retrieval by using a Bins instance as an index for each required configuration of data.

Origins
=======

In the process of having to read, parse, validate, classify, and store (in multiple ways) television-program scheduling data, I needed an efficient method to store the data. Here, efficiency meant fast to load, and fast to store into multiple, concurrent indices.

Example Usage
=============

Import the functionality. We're primarily interested in Bins (each instance of which will be referred to as an "index" so as to not be ambiguous between the Bins object and the bin files, themselves), but we also need to tell the Bins instance how to sort the data. We want to use the SORT_BYKEY strategy.

    from pybufferbins.bins import Bins, SORT_BYKEY

For the purpose of the example, there have been some Protocol Buffer types 
imported.

    SdProgram
    SdSchedule

To configure the index, instantiate with the name of a directory to store the bins in. You must add handlers for every type of record that will be pushed into the bins. The method also requires the name of the field on the record that will be used to group the records into bins.

    programs = Bins('sd_bins/by_program', SORT_BYKEY)

    programs.add_handler(SdProgram, 'Program')
    programs.add_handler(SdSchedule, 'Program')

Push each incoming record:

    programs.push(schedule)

You may push to any number of indices simultaneously. All indices are thread-safe.

Make sure to do a flush after all pushes are complete:

    programs.flush()

Example Scenario
================

From a home system, 5170 programs describing a day's worth of television programs, along with additional data describing stations, schedules, program-station-channel mappings, actors, and genre records, were downloaded and stored across three different bins-configurations ("indices") containing a total of 8251 bins in fourteen seconds.

$ time PYTHONPATH=. ./test.py 
SchedulesDirect(USERNAME=dsoprea)

real	0m14.565s
user	0m2.504s
sys	0m0.316s

==> DATA LOADED INTO MULTIPLE SETS OF BINS

$ ls -l sd_bins/
total 136
drwxrwxr-x    3 dustin dustin   4096 Jan 23 21:14 by_lineup
drwxrwxr-x 3067 dustin dustin 131072 Jan 23 21:14 by_program
drwxrwxr-x  186 dustin dustin   4096 Jan 23 21:14 by_station

==> PROGRAM-INFO

$ ls -l sd_bins/by_program/SH016794860000
total 12
-rw-rw-r-- 1 dustin dustin 124 Jan 23 21:14 SdProgram
-rw-rw-r-- 1 dustin dustin  44 Jan 23 21:14 SdProgramCrew
-rw-rw-r-- 1 dustin dustin  63 Jan 23 21:14 SdProgramGenre

$ hexdump -C sd_bins/by_program/SH016794860000/SdProgram
00000000  7a 00 0a 0e 53 48 30 31  36 37 39 34 38 36 30 30  |z...SH0167948600|
00000010  30 30 12 0a 45 50 30 31  36 37 39 34 38 36 1a 0e  |00..EP01679486..|
00000020  50 72 6f 66 65 73 73 6f  72 20 49 72 69 73 2a 3e  |Professor Iris*>|
00000030  53 63 68 6f 6c 61 72 6c  79 20 62 69 72 64 20 74  |Scholarly bird t|
00000040  65 61 63 68 65 73 20 6c  65 73 73 6f 6e 73 20 74  |eaches lessons t|
00000050  68 72 6f 75 67 68 20 6d  61 67 69 63 2c 20 73 6f  |hrough magic, so|
00000060  6e 67 73 20 61 6e 64 20  68 75 6d 6f 72 2e 50 04  |ngs and humor.P.|
00000070  62 0a 31 39 39 32 2d 31  32 2d 32 38              |b.1992-12-28|
0000007c

==> USING TOOL TO DUMP FILE

$ PYTHONPATH=. tools/dump_bin.py 
Please provide <module> <class name> <file to read>

$ PYTHONPATH=. tools/dump_bin.py mediaconsole.data.protocol_buffer.schedules_direct.sd_pb2 SdProgram sd_bins/by_program/MV000120430000/SdProgram

Program: "MV000120430000"
Title: "First Blood"
Description: "Green Beret veteran Rambo (Sylvester Stallone) takes on a Pacific Northwest sheriff (Brian Dennehy) and the National Guard."
MpaaRating: R
StarRating: "***"
RunTime: 95
Year: "1982"
Advisory: Adult_Situations
Advisory: Language
Advisory: Brief_Nudity
Advisory: Graphic_Violence

$ PYTHONPATH=. tools/dump_bin.py mediaconsole.data.protocol_buffer.schedules_direct.sd_pb2 SdProgramCrew sd_bins/by_program/MV000120430000/SdProgramCrew 

Program: "MV000120430000"
Role: "Actor"
FullName: "Sylvester Stallone"

Program: "MV000120430000"
Role: "Actor"
FullName: "Richard Crenna"

Program: "MV000120430000"
Role: "Actor"
FullName: "Brian Dennehy"

(15 records total)


