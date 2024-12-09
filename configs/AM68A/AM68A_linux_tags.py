# Device Family is J721S2 = Jacinto 7 AEP
fam_name = 'AM68A'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families
project = u'Processor SDK Linux for AM68A'
html_title = 'Processor SDK Linux for AM68A Documentation'

# The master toctree document.
master_doc = 'devices/J7_Family/linux/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['rtos', 'android', 'linux/index.rst', 'devices/AM335X', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/J7200', 'devices/J721E', 'devices/J784S4', 'devices/DRA821A', 'devices/AM62X', 'devices/AM62AX']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'
