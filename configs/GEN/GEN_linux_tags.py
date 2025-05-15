# Device Family is GEN = General family
fam_name = 'GEN'

# Processor SDK Linux documentation build configuration file

# The master toctree document.
master_doc = 'linux/index'

# Output file base name for HTML help builder.
htmlhelp_basename = 'ProcessorSDKLinuxdoc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'ProcessorSDKLinux.tex', u'Processor SDK Linux Documentation',
   u'Texas Instruments Incorporated', u'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ProcessorSDKLinux', u'Processor SDK Linux Documentation',
     ['Texas Instruments Incorporated'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'ProcessorSDKLinux', u'Processor SDK Linux Documentation',
   'Texas Instruments Incorporated', 'ProcessorSDKLinux', 'One line description of project.',
   'Miscellaneous'),
]
