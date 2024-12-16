#!/bin/sh

# find files that incorrectly include top level files

rg -i '.. include:: .*/[^_\/]+[^\/]*\.rst' source/
