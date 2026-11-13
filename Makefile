# User defined variables for Sphinx
SPHINXOPTS     ?=
SPHINXBUILD    ?= sphinx-build
SOURCEDIR       = source

# User defined variables for custom plugins
DEVFAMILY      ?= AM62X
OS             ?= linux

# Case modification functions, to assist with custom plugins
_UC = $(shell printf '%s' '$(1)' | tr '[:lower:]' '[:upper:]')
_LC = $(shell printf '%s' '$(1)' | tr '[:upper:]' '[:lower:]')

# Export variable overrides for custom plugins
override DEVFAMILY      := $(call _UC,$(DEVFAMILY))
override OS             := $(call _LC,$(OS))
override ROOTDIR        := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
export DEVFAMILY OS ROOTDIR

# Configuration directory, complicated because of Jacinto
CONFDIR = $(SOURCEDIR)/devices/$(DEVFAMILY)/$(OS)
ifneq ($(filter $(DEVFAMILY), J721E J7200 J721S2 J784S4 AM68 AM69 J722S AM67 J742S2 AM68A AM67A AM69A TDA4VM),)
  # For Linux and other OSes, use J7_Family
  CONFDIR = $(SOURCEDIR)/devices/J7_Family/$(OS)
  ifeq ($(OS), android)
    # For Android, AM67A has their own device directories
    ifneq ($(filter $(DEVFAMILY), AM67 AM67A),)
      CONFDIR = $(SOURCEDIR)/devices/$(DEVFAMILY)/$(OS)
    endif
  endif
  # Print the new variable since this logic is likely to break
  $(info CONFDIR = "$(CONFDIR)")
endif

# These can be overridden if necessary
VERSION         = $(file <$(CONFDIR)/version.txt)

# TI specifc deployment variables
BUILDDIR        = build/processor-sdk-$(OS)-$(DEVFAMILY)
ti : BUILDDIR   = build/processor-sdk-$(OS)-$(DEVFAMILY)/esd/docs/$(VERSION)

# Internal additions to SPHINXOPTS
CONFLOC         = -c $(ROOTDIR)
VEROPTS         = -D version=$(VERSION) -D release=$(VERSION)
GIT_HASH        = -D html_context.commit="$(shell git rev-parse --short HEAD)"
DOCTREE         = -d $(BUILDDIR)/doctrees
SPHINXOPTS     := $(strip $(CONFLOC) $(VEROPTS) $(GIT_HASH) $(DOCTREE) $(SPHINXOPTS))

# Give some information on the command line about the build
$(info DEVFAMILY = "$(DEVFAMILY)")
$(info OS = "$(OS)")
$(info ROOTDIR = "$(ROOTDIR)")
$(info VERSION = "$(VERSION)")
$(info BUILDDIR = "$(BUILDDIR)")

.PHONY: default lint

default: ti

lint:
	rstcheck -r "$(SOURCEDIR)"

# Backwards compatible build target that preserves the old output path, for now
ti:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# Pass everything else back to Sphinx, as they have their own "help" function to
# list available builders, and their own "clean" function
%::
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
