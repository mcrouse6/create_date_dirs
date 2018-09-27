#!/usr/bin/env python
import argparse
import time
from util import parseDate, createDirectoryTuple, createDateDirHelper 
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

    directories_tuple_list = createDirectoryTuple(start_date, end_date, args.keep_file) 
    
    start = time.time()
    pool = Pool(processes=8)
    pool.map(createDateDirHelper, directories_tuple_list)

    if args.verbose:
      print("Directory creation time: {}".format(time.time() - start))
    

