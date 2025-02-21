# Device Family is AM335X = AM335X family
fam_name = 'AM335X'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families
project = u'Processor SDK Linux for AM335X'
html_title = 'Processor SDK Linux for AM335X Documentation'

# The master toctree document.
master_doc = 'devices/AM335X/linux/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['rtos', 'android', 'linux/index.rst', 'devices/AM335X/rtos', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/J7_Family', 'devices/DRA821A', 'devices/AM62X', 'devices/AM62AX', 'devices/AM62PX', 'devices/AM62LX']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'
