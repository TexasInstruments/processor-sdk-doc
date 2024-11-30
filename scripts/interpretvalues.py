import os, re

# This script fills all the replacevars that will be replaced in the documentation
# source code.  It also will add config values (for use by 'ifconfig' directive).

text = []

# read_familyvals
# ---------------
# Description:
#
# Parameters: app             - Application calling this Python function
#             valuesfile      - Device family input configuration file
#             fam_replacevars - Hash table for all the replacement variables defined in
#                               <DEVICE_FAMILY>_config.txt
#             fam_configvals  - Hash table for all the configuration values defined
#                               in <DEVICE_FAMILY>_config.txt
#                               (i.e. each has name, key pairs)

def read_familyvals(valuesfile):
    fam_replacevars = {}
    fam_configvals = {}
    filt_hash_pair = [None] * 2
    with open("configs" + os.sep + valuesfile, 'r') as f:
        text = f.readlines() # read text lines to list
        for index, line in enumerate(text):
            # Interpret shared variables first (which should always be listed first)
            match = re.match(r'Replacement Variables', re.sub(r"\n\t\s]*", "", line))
            if match:
                # Replacement Variables start 2 lines after "Replacement Variables" title
                subcontents = text[index+2:]
                # Find next non-empty line to start reading the shared variables
                start_of_vars = next(i for i, x in enumerate(subcontents) if x.rstrip('\n'))
                subcontents = subcontents[start_of_vars:]
                for j in subcontents:
                    if j.strip() == '':
                        # Last blank line after Replacement Variable definition
                        break
                    # Strip trailing ",\n" and split line into hash table pair
                    # (based on first instance of ':' character)
                    test_line = j.rstrip(',\n')
                    hash_pair = test_line.split(":", 1)
                    for k, hash_item in enumerate(hash_pair):
                        # Trim all leading and trailing spaces, and the single quotes
                        filt_hash_item = hash_item.strip()
                        filt_hash_item = filt_hash_item.strip("\'")
                        filt_hash_pair[k] = filt_hash_item
                    fam_replacevars[filt_hash_pair[0]] = filt_hash_pair[1]
            # Interpret configuration values first (which should always be listed second)
            match = re.match(r'Configuration Values', re.sub(r"\n\t\s]*", "", line))
            if match:
                # Configuration values start 2 lines after "Configuraiton Values" title
                subcontents = text[index+2:]
                # Find next non-empty line to start reading the configuration values
                start_of_vars = next(i for i, x in enumerate(subcontents) if x.rstrip('\n'))
                subcontents = subcontents[start_of_vars:]
                for j in subcontents:
                    if j.strip() == '':
                        # Last blank line after Configuration values definition
                        break
                    # Strip trailing ",\n" and split line into hash table pair
                    # (based on first instance of ':' character)
                    test_line = j.rstrip(',\n')
                    hash_pair = test_line.split(":", 1)
                    for k, hash_item in enumerate(hash_pair):
                        # Trim all leading and trailing spaces, and the single quotes
                        filt_hash_item = hash_item.strip()
                        filt_hash_item = filt_hash_item.strip('\'')
                        filt_hash_pair[k] = filt_hash_item
                    # Fill fam_configvals hash table
                    fam_configvals[filt_hash_pair[0]] = filt_hash_pair[1]
    return (fam_replacevars, fam_configvals)
