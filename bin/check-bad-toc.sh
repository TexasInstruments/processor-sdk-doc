#!/bin/bash

# make sure the toc tree isn't including files that are supposed to be included
# by other files

find configs/ -name '*_toc.txt' -print0 | 
	while IFS= read -r -d '' file_name; do 
		rg -i '.*/_[^\/]*' "$file_name"
	done
