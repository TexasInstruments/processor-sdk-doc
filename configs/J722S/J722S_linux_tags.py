# Device Family name
fam_name = 'J722S'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families

project = u'Processor SDK Linux for J722S'
html_title = 'Processor SDK J722S Documentation'

# The master toctree document.
master_doc = 'devices/J7_Family/linux/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

# J722S RTOS docs are not in this project, rather referenced externally,
# so exclude 'rtos' folder along with others.
exclude_patterns = ['android', 'files', 'rtos', 'devices/AM335X', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/DRA821A', 'devices/AM62AX', 'devices/AM62PX', 'devices/AM62LX']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'


