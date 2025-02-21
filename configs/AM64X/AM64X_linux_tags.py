# Device Family name
fam_name = 'AM64X'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families

project = u'Processor SDK Linux for AM64X'
html_title = 'Processor SDK AM64X Documentation'

# The master toctree document.
master_doc = 'devices/AM64X/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

# AM64x RTOS docs are not in this project, rather referenced externally,
# so exclude 'rtos' folder along with others.
exclude_patterns = ['android', 'example_code', 'files', 'rtos', 'devices/AM335X', 'devices/AM437X', 'devices/AM65X', 'devices/J7_Family', 'devices/DRA821A' , 'devices/AM62X', 'devices/AM62AX', 'devices/AM62PX', 'devices/AM62LX']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'


