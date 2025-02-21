# Device Family is DRA821A = MPU-only Jacinto 7 VCL
fam_name = 'DRA821A'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families
project = u'Processor SDK Linux for DRA821A'
html_title = 'Processor SDK Linux for DRA821A Documentation'

# The master toctree document.
master_doc = 'devices/DRA821A/linux/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['rtos', 'android', 'linux/index.rst', 'devices/AM335X', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/J7_Family', 'devices/AM62X', 'devices/AM62AX', 'devices/AM62PX', 'devices/AM62LX']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'
