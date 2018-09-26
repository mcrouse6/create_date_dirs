#!/usr/bin/env python
import argparse
import time
from util import parseDate, createDateDirectories


if __name__ == "__main__":

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

    start = time.time()
    global_start = start

    createDateDirectories(start_date, end_date, args.keep_file)

    if args.verbose:
        print("Total runtime: {}".format(time.time()- global_start))
    

