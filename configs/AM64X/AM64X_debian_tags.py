# Device Family name
fam_name = 'AM64X'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families

project = u'Debian for AM64x'
html_title = 'Debian AM64x Documentation'

# The master toctree document.
master_doc = 'devices/AM64X/debian/index'

# AM64x RTOS docs are not in this project, rather referenced externally,
# so exclude 'rtos' folder along with others.

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'debian'


