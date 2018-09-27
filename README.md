# Date Directory Command Line Utility

This a command line tool that will take as input a start date and an end date and will create a directory (folder) tree structure on disk with a distinct root directory for each year in the range specified.  Each year directory has sub directories for each month and each month has subdirectories for each day within that month. 

Additionally, the utility allows for an optional argument to allow the user  to indicate that a keep file is created in each directory. The keep file with the name “.keep” is placed in each and every created directory.


## Installation Notes
The command line was built using a vanilla python3 (ver. 3.6.5) and requires no additional outside dependencies.
To configure for execution, your local system must have python3 installed. 

To install on your local machine, you can clone the public repo that the code resides: 

```
git clone https://github.com/mcrouse6/create_date_dirs.git
```

The code can also be downloaded from the repo page via zip file [here](https://github.com/mcrouse6/create_date_dirs)

If you would like to execute as a tool without calling python3, you can set the permissions of the utility to be executeable, 
for a Linux system this can be done with the following command:

```
chmod u+x create_date_dirs.py
```

## Usage Details


For information about the arguments to the utility, including the keep functionality, you can look at the included help function:

```
./create_date_dirs.py --help
```

and its output is:

```
usage: create_date_dirs.py [-h] --start_date START_DATE --end_date END_DATE
                           [--keep_file] [--verbose]

This programs creates some date-based directories for receiving data files.

optional arguments:
  -h, --help            show this help message and exit
  --start_date START_DATE
                        Start of date range (format: YYYY-MM-DD) to generate
                        date-based directories
  --end_date END_DATE   End of date range (format: YYYY-MM-DD) to generate
                        date-based directories
  --keep_file           If set, an empty ".keep" file will be placed in every
                        directory created
  --verbose             If set, more verbose reporting will be done
```


## Examples

1. Date range without keep files: 
- to create a set of directories as described above (based on a date range):

```
./create_date_dirs.py --start_date 2000-02-01 --end_date 2001-03-05 
```

2. Date range with keep files generated:


```
./create_date_dirs.py --start_date 2000-02-01 --end_date 2001-03-05 --keep_file
```

