import os, re

# This script handles section inclusion/exclusion for the device family

toctreefiles    = []
toctreesections = []
docs_to_keep    = []
all_rst_files   = []

# fill_docs_to_keep
# -----------------
#
# Description: Opens the device family Table-of-Contents file and reads each of the lines
#              into the docs_to_keep[] array
#
# Parameters: app               - Application calling this Python function
#             family_configlist - Device family Table-of-Contents file input
#             verbosity         - Flag to determine if function will print names for all
#                                 documents that are to be included

def fill_docs_to_keep(app, family_configlist, verbosity):
    for config in family_configlist:
        with open("configs" + os.sep + config, 'r') as docconfigfile:
            for line in docconfigfile:
                if line.strip():
                    # Only add line to docs_to_keep[] if it is not a blank line
                    docs_to_keep.append(re.sub(r"[\n\t\s]*", "", line))
    if verbosity == 1:
        print("The following .rst files will be included in the build:")
        print('[')
        for elem in docs_to_keep:
            print(elem)
        print(']')

# set_excluded_docs
# -----------------
#
# Description:  For each file in all_rst_files, searches the docs_to_keep[] array
#               for its explicit inclusion in the device family build.  If the file
#               is not found, it is placed in the exclusion_list so that Sphinx does not build it.
#
# Parameters: app            - Application calling this Python function
#             exclusion_list - Section (.rst file) exclusion list used by Sphinx build

def set_excluded_docs(app, exclusion_list):
    for entry in all_rst_files:
        #print("Checking " + entry)
        if entry[:-4] not in docs_to_keep: # use [:-4] to remove ".rst" at the end
            #print("Removing " + entry)
            exclusion_list.append(entry)

# find_toctree_files
# ------------------
#
# Description:  Recursively searches for all files in the source folder (except those in excluded_patters)
# that contain "toctree" directives, and places the names of these files in toctreefiles[].
#
# Parameters: app             - Application calling this Python function
#             exclude_in_conf - excluded_patterns from <device>_tags.py

def find_toctree_files(app, exclude_in_conf):
    directory=os.getcwd() + os.sep + "source"
    #print("Running find_toctree_files: directory = " + directory)
    for root, dirs, files in os.walk(directory):
        # exclude directories specified by excluded_patters in <device>_tags.py
        dirs[:] = [d for d in dirs if (os.path.join(root, d).replace(directory+"/", "")) not in exclude_in_conf]
        for filename in files:
            if filename.endswith(".rst") and os.path.join(root, filename).replace(directory+"/", "") not in exclude_in_conf:
                #print("Checking " + filename)
                path = os.path.join(root, filename)
                f = open(path, 'r')

                if "toctree" in f.read():
                    #print('found string in file %s' % filename)
                    toctreefiles.append(path)
                f.close()
    #print("Finished toctree file search")
    #print(toctreefiles)

# find_all_rst_files
# ------------------
#
# Description: Recursively finds all .rst files in the source directory, excluding those
#              defined in excluded_patterns from <device>_tags.py
#
# Parameters: app             - Application calling this Python function
#             exclude_in_conf - excluded_patterns from <device>_tags.py

def find_all_rst_files(app, exclude_in_conf):
    extension = '.rst'
    directory = "source"
    for dirpath, dirnames, files in os.walk(directory):
        # exclude directories specified by excluded_patters in <device>_tags.py
        dirnames[:] = [d for d in dirnames if (os.path.join(dirpath, d)).replace("source/", "") not in exclude_in_conf]
        for name in files:
            if extension and name.lower().endswith(extension) and os.path.join(dirpath, name).replace("source/", "") not in exclude_in_conf :
                rst_path = os.path.join(dirpath, name)
                all_rst_files.append(rst_path.replace("source/",""))
    #print("Finished .rst file search")
    #print(all_rst_files)

# get_toctree_entries
# -------------------
#
# Description:  This function opens a toctreenodefile that contains a "toctree" directive within it.
# It searches for the "toctree" directive. After finding the toctree directive, it searches
# for the next blank line (since this blank line is required for toctree's to work
# in restructured text).  It then reads each line into toctreesections[] until it encounters
# another blank line.
#
# Limitations:  In the current implementation, the assumption is that only a single toctree directive
# is in each file.  This code would need to be updated if more than one toctree directive
# is found in a single file.
#
# Parameters: app             - Application calling this Python function
#             toctreenodefile - An .rst file that contains a toctree directive

def get_toctree_entries(app, toctreenodefile):
    with open(toctreenodefile, 'r') as tocfile:
        line = 1
        cnt = 0
        while line:
            line = tocfile.readline()
            cnt += 1
            # Searching for "toctree" line
            toctreeline = re.match(r'^\.\. toctree::', line)
            if toctreeline:
                break
        while line:
            # Searching for next blank line
            line = tocfile.readline()
            cnt += 1
            if not line.strip():
                #print("Found blank line at line " + "{}".format(cnt))
                break
        while line:
            # Reading lines and filling section array until next blank line
            line = tocfile.readline()
            cnt += 1
            if line.strip() == '':
                #print("Found last blank line")
                break
            # First, search for location of this .rst
            rstfilename = "/" + re.sub(r"[\n\t\s]*", "", line) + ".rst"
            rstfilelocation = [s for s in all_rst_files if rstfilename in s]
            if len(rstfilelocation) > 1:
                print("Error - More than one .rst file has been found for this TOC entry: ")
                for i, value in enumerate(rstfilelocation):
                    print(rstfilelocation[i])
            elif len(rstfilelocation) == 0:
                print("Error - .RST file has not been found for " + rstfilename + " section used in toctree.")
                raise Exception('.RST file missing for section used in toctree.')
            else:
                # Only 1 string has been found in the .rst array
                rststring = rstfilelocation[0]
                if rststring:
                    # Append the found .rst file to the toctreesections list
                    toctreesections.append(re.sub(r'\.rst$', '', rststring))
                else:
                    print("TOC Tree Entry is not a defined .rst file in current directory")


# create_master_rst_list
# ----------------------
#
# Description:  This function first recursively searches for all files in source/{op_os} folder
# that contain "toctree" directives, and places the names of these files in toctreefiles[].
# Second, it recursively searches in this same directory for all .rst files and places the
# names of these files in all_rst_files[].
# Lastly, it gathers the toctreesections[] across all the toctreefiles[].
# The result of this function is a master list (in toctreesections[]) of all .rst files
# that the Table of Contents stage of the Sphinx build could utilize.
#
# Parameters: app             - Application calling this Python function
#             exclude_in_conf - excluded_patterns from <device>_tags.py

def create_master_rst_list(app, exclude_in_conf):
    find_toctree_files(app, exclude_in_conf)
    find_all_rst_files(app, exclude_in_conf)
    #print(toctreefiles)
    for files in toctreefiles:
        get_toctree_entries(app, files)
    #for section in toctreesections:
    #    print(section)
