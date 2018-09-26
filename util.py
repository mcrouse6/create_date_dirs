import os
import time
from datetime import datetime, timedelta

BASE_DIR = "test_dir"

def parseDate(input_date, date_str):
    try:
        return datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("The specified %s date is invalid - the required format is YYYY-MM-DD" % (date_str))
    
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
    visited_map = {}
    while cur_date <= end_date:
        date_pth = "{}/{:04d}/{:02d}/{:02d}".format(BASE_DIR, cur_date.year, cur_date.month, cur_date.day)
        directory_list.append(date_pth)
        if keep_file:
            if cur_date.year not in visited_map:
                directory_list.append("{}/{:04d}".format(BASE_DIR, cur_date.year))
                keep_file_list.append("{}/{:04d}/{}".format(BASE_DIR, cur_date.year, keep_file_name))
                visited_map[cur_date.year] = True

            if str(cur_date.year)+str(cur_date.month) not in visited_map:
                visited_map[str(cur_date.year)+str(cur_date.month)] = True
                directory_list.append("{}/{:04d}/{:02d}".format(BASE_DIR, cur_date.year, cur_date.month))
                keep_file_list.append("{}/{:04d}/{:02d}/{}".format(BASE_DIR, cur_date.year, cur_date.month,  keep_file_name))

            keep_file_list.append("{}/{}".format(date_pth,  keep_file_name))
        cur_date += day_delta

            
    return directory_list, keep_file_list
        
def printReport(directories, keep_file_list):
    print("Date Directory Summary Report")
    print("Directories created: {}".format(len(directories)))
    if len(keep_file_list) > 0:
        print("Keeper Files created: {}".format(len(directories)))

        