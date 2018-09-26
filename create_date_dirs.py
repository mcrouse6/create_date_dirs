#!/usr/bin/env python
import argparse
import time
from util import parseDate, createDirectoryList, createKeepFile, createDirectory, printReport, createDateDirectories 
from multiprocessing import Pool


if __name__ == "__main__":

    # Initial cmd line argument parsing
    parser = argparse.ArgumentParser(description='This programs creates some date-based directories for receiving data files.')
    parser.add_argument('--start_date', 
                            required=True, 
                            type=str,
                            help="Start of date range to generate date-based directories")
    parser.add_argument('--end_date', 
                            required=True, 
                            type=str,
                            help="End of date range to generate date-based directories")
    parser.add_argument('--keep_file',
                            action='store_true',
                            help='If set, an empty ".keep" file will be placed in every directory created' )
    parser.add_argument('--verbose',
                            action='store_true',
                            help='If set, more verbose reporting will be done')

    args = parser.parse_args()

    keep_file_name = ".keep"

    start_date = parseDate(args.start_date, "start")
    end_date = parseDate(args.end_date, "end")


    if args.verbose:
      start = time.time()
      global_start = start
    #createDateDirectories(start_date, end_date, args.keep_file)

    directories, keep_file_list = createDirectoryList(start_date, end_date, args.keep_file)

    if args.verbose:
      print("File list generation time: {}".format(time.time() - start))

    start = time.time()
    pool = Pool(processes=8)
    pool.map(createDirectory, directories)

    if args.verbose:
      print("Directory creation time: {}".format(time.time() - start))

    if len(keep_file_list) > 0:
        start = time.time()
        pool.map(createKeepFile, keep_file_list)
        if args.verbose:
          print("Keep file creation time: {}".format(time.time() - start))


    if args.verbose:
      printReport(directories, keep_file_list)
      print("Total runtime: {}".format(time.time()- global_start))
    

