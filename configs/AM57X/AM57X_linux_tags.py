# Device Family is AM57X = AM57X family
fam_name = 'AM57X'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families
project = u'Processor SDK Linux for AM57X'
html_title = 'Processor SDK Linux for AM57X Documentation'

# The master toctree document.
master_doc = 'devices/AM57X/linux/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['rtos', 'android', 'linux/index.rst', 'devices/AM57X/rtos', 'devices/AM335X', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/J7_Family', 'devices/DRA821A', 'devices/AM62X', 'devices/AM62AX', 'devices/AM62PX', 'devices/AM62LX']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'
