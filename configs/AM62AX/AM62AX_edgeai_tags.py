# Device Family name
fam_name = 'AM62AX'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families

project = u'Processor SDK Linux Edge AI for AM62Ax'
html_title = 'Processor SDK AM62Ax Documentation'

# The master toctree document.
master_doc = 'devices/AM62AX/edgeai/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

# AM62A RTOS docs are not in this project, rather referenced externally,
# so exclude 'rtos' folder along with others.
exclude_patterns = ['android', 'example_code', 'files', 'rtos', 'devices/AM335X', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/TDA4VM', 'devices/J7200', 'devices/AM67A', 'devices/AM68A', 'devices/AM69A', 'devices/DRA821A']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'edgeai'


