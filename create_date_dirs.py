import argparse
import os
import time
from datetime import datetime, timedelta


BASE_DIR = "test_dir"

# format_map = { "year" : {"format_str" : "{:04d}", "min_start" : 1, "max_end" : 9999  }},
#                "month" : {"format_str" : "{:02d}", "min_start" : 1, "max_end" : 12  }},
#                "day" : {"format_str" : "{:02d}", "min_start" : 1, "max_end" : 31  }},
#                "hour" : {"format_str" : "{:02d}", "min_start" : 1, "max_end" : 24  }} }

def parseDate(input_date, date_str):
    try:
        return datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("The specified %s date is invalid - the required format is YYYY-MM-DD" % (date_str))
    
def isLeapYear(d):
    if d.year % 4 == 0:
        if d.year % 100 == 0 and d.year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def createDirectory(dir_pth):
    try:
        if not os.path.exists(dir_pth):
            os.makedirs(dir_pth)
        else:
            # directory already made
            pass
    except:
        raise OSError("Cannot create the create directory: {}".format(dir_pth))


def createKeepFile(file_pth):
    try:
        dir_pth = "/".join(file_pth.split("/")[:-1])
        if os.path.exists(dir_pth):
            with open(file_pth, 'a'):
                os.utime(file_pth, None)
        else:
            # directory does not exist
            raise ValueError("Expected Directory/path does not exist to create file: {}".format(file_pth))
    except:
        raise OSError("Cannot create the file: {}".format(file_pth))

def generateDateRanges(pth, start, end, output_fmt):
    directory_list = []
    for i in range(start, end+1):
        tmp_pth = pth + output_fmt.format(i) 
        directory_list.append(tmp_pth)
    return directory_list

def createDirectoryList(start_date, end_date, keep_file=None, keep_file_name=".keep"):
    directory_list = []
    keep_file_list = []

    day_delta = timedelta(days=1)
    cur_date = start_date
    years_seen = {}
    months_seen = {}
    while cur_date <= end_date:
        date_pth = "{}/{:04d}/{:02d}/{:02d}".format(BASE_DIR, cur_date.year, cur_date.month, cur_date.day)
        directory_list.append(date_pth)
        if keep_file:
            if cur_date.year not in years_seen:
                directory_list.append("{}/{:04d}".format(BASE_DIR, cur_date.year))
                keep_file_list.append("{}/{:04d}/{}".format(BASE_DIR, cur_date.year, keep_file_name))
                years_seen[cur_date.year] = True

            if str(cur_date.year)+str(cur_date.month) not in months_seen:
                months_seen[str(cur_date.year)+str(cur_date.month)] = True
                directory_list.append("{}/{:04d}/{:02d}".format(BASE_DIR, cur_date.year, cur_date.month))
                keep_file_list.append("{}/{:04d}/{:02d}/{}".format(BASE_DIR, cur_date.year, cur_date.month,  keep_file_name))

            keep_file_list.append("{}/{}".format(date_pth,  keep_file_name))
        cur_date += day_delta

            
    return directory_list, keep_file_list

"""
def createDirectoryList(start_date, end_date, keep_file=None):

    directory_list = []
    keep_file_list = []
    full_year = False
    full_month = False

    for y in range(start_date.year, end_date.year+1):
        if y == end_date.year or y == start_date.year:     # partial date - start or end 
            if y == start_date.year and y == end_date.year: #  partial case in same year
                year_pth = "{}/{:04d}".format(BASE_DIR, y)
                directory_list.append(createDirectory(year_pth))
                if keep_file:
                    keep_file_list.append(createKeepFile(year_pth, keep_file_name))

                # create all 12 month directories
                for m in range(start_date.month,end_date.month+1):



            elif y == start_date.year:  # first year
                year_pth = "{}/{:04d}".format(BASE_DIR, y)
                directory_list.append(createDirectory(year_pth))
                if keep_file:
                    keep_file_list.append(createKeepFile(year_pth, keep_file_name))

                # create all 12 month directories
                for m in range(start_date.month,13):
                    month_pth = "{}/{:02d}".format(year_pth, m)
                    directory_list.append(createDirectory(month_pth))
                    if keep_file:
                        createKeepFile(month_pth, keep_file_name)

                    if m == start_date.month:    
                        # create all days in days_per_month map 
                        for d in range(start_date.day, days_per_month[m]):
                            day_pth = "{}/{:02d}".format(month_pth, d)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name)

                        if m == 2 and isLeapYear(y): # short-circuit and check for leap year
                            day_pth = "{}/{:02d}".format(month_pth, 29)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name)
                    else:
                        for d in range(1, days_per_month[m]):
                            day_pth = "{}/{:02d}".format(month_pth, d)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name)

                        if m == 2 and isLeapYear(y): # short-circuit and check for leap year
                            day_pth = "{}/{:02d}".format(month_pth, 29)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name) 

            

            elif y == end_date.year:    # last year 
                year_pth = "{}/{:04d}".format(BASE_DIR, y)
                directory_list.append(createDirectory(year_pth))
                if keep_file:
                    keep_file_list.append(createKeepFile(year_pth, keep_file_name))

                # create all 12 month directories
                for m in range(1,end_date.month+1):
                    month_pth = "{}/{:02d}".format(year_pth, m)
                    directory_list.append(createDirectory(month_pth))
                    if keep_file:
                        createKeepFile(month_pth, keep_file_name)

                    if m != end_date.month:  # last month    
                        # create all days in days_per_month map 
                        for d in range(start_date.day, days_per_month[m]):
                            day_pth = "{}/{:02d}".format(month_pth, d)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name)

                        if m == 2 and isLeapYear(y): # short-circuit and check for leap year
                            day_pth = "{}/{:02d}".format(month_pth, 29)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name)
                    else:
                        for d in range(1, end_date.day+1):
                            day_pth = "{}/{:02d}".format(month_pth, d)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name)

                        if m == 2 and isLeapYear(y) and end_date.day == 29: # short-circuit and check for leap year
                            day_pth = "{}/{:02d}".format(month_pth, 29)
                            directory_list.append(createDirectory(day_pth))
                            if keep_file:
                                createKeepFile(day_pth, keep_file_name) 

        else:
            year_pth = "{}/{:04d}".format(BASE_DIR, y)
            directory_list.append(createDirectory(year_pth))
            if keep_file:
                keep_file_list.append(createKeepFile(year_pth, keep_file_name))

            # create all 12 month directories
            for m in range(1,13):
                month_pth = "{}/{:02d}".format(year_pth, m)
                directory_list.append(createDirectory(month_pth))
                if keep_file:
                    createKeepFile(month_pth, keep_file_name)
                
                # create all days in days_per_month map 
                for d in range(1, days_per_month[m]):
                    day_pth = "{}/{:02d}".format(month_pth, d)
                    directory_list.append(createDirectory(day_pth))
                    if keep_file:
                        createKeepFile(day_pth, keep_file_name)

                if m == 2 and isLeapYear(y): # short-circuit and check for leap year
                    day_pth = "{}/{:02d}".format(month_pth, 29)
                    directory_list.append(createDirectory(day_pth))
                    if keep_file:
                        createKeepFile(day_pth, keep_file_name)
                    

            
    return directory_list
"""

        
def printReport(directories, keep_file_list):
    print("Date Directory Summary Report")
    print("Directories created: {}".format(len(directories)))
    if len(keep_file_list) > 0:
        print("Keeper Files created: {}".format(len(directories)))

        
days_per_month = {1 : 31, 
                  2 : 28,
                  3 : 31,
                  4 : 30,
                  5 : 31,
                  6 : 30,
                  7 : 31,
                  8: 31, 
                  9 : 30,
                  10 : 31, 
                  11 : 30,
                  12 : 31}

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

    args = parser.parse_args()

    keep_file_name = ".keep"

    start_date = parseDate(args.start_date, "start")
    end_date = parseDate(args.end_date, "end")


    if start_date > end_date:
        raise ValueError( "Start date must occur before provide end date")

    start = time.time()
    directories, keep_file_list = createDirectoryList(start_date, end_date, args.keep_file)
    print("File list generation time: {}".format(time.time() - start))

    start = time.time()
    [createDirectory(d) for d in directories] 
    print("Directory creation time: {}".format(time.time() - start))

    if len(keep_file_list) > 0:
        start = time.time()
        [createKeepFile(p) for p in keep_file_list]
        print("Keep file creation time: {}".format(time.time() - start))

    printReport(directories, keep_file_list)

