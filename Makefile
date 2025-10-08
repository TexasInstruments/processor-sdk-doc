# Makefile for Sphinx documentation
#

default: html

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
OS           ?= linux

_UC = $(shell echo '$1' | tr '[:lower:]' '[:upper:]')
_LC = $(shell echo '$1' | tr '[:upper:]' '[:lower:]')

DEVFAMILY_UP=$(call _UC,${DEVFAMILY})
OS_LOW=$(call _LC,${OS})

mkfile_path = $(abspath $(lastword $(MAKEFILE_LIST)))
export ROOTDIR = $(dir $(mkfile_path))
$(info ROOTDIR is $(ROOTDIR))

$(info DEVFAMILY is $(DEVFAMILY_UP))

ifeq ($(OS_LOW), android)
  # For Android, AM67A and AM67 have their own device directories
  ifeq ($(DEVFAMILY_UP), $(filter $(DEVFAMILY_UP), J721E J7200 J721S2 J784S4 AM68 AM69 J722S J742S2 AM68A AM69A TDA4VM))
    CONFDIR = source/devices/J7_Family/${OS_LOW}
  else
    CONFDIR = source/devices/$(DEVFAMILY_UP)/${OS_LOW}
  endif
else
  # For Linux and other OSes, use J7_Family grouping including AM67A and AM67
  ifeq ($(DEVFAMILY_UP), $(filter $(DEVFAMILY_UP), J721E J7200 J721S2 J784S4 AM68 AM69 J722S AM67 J742S2 AM68A AM67A AM69A TDA4VM))
    CONFDIR = source/devices/J7_Family/${OS_LOW}
  else
    CONFDIR = source/devices/$(DEVFAMILY_UP)/${OS_LOW}
  endif
endif

$(info CONFDIR is $(CONFDIR))

VERSION   = $(shell cat ${CONFDIR}/version.txt)
SOURCEDIR = source
BUILDDIR  = build/processor-sdk-${OS_LOW}-${DEVFAMILY_UP}/esd/docs/${VERSION}

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from https://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
CONFLOC         = -c $(ROOTDIR)
VEROPTS         = -D version=${VERSION} -D release=${VERSION}
GIT_HASH        = -D html_context.commit="$(shell git rev-parse --short HEAD)"
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(CONFLOC) $(VEROPTS) $(GIT_HASH)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean config html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"

clean:
	rm -rf "$(BUILDDIR)"

lint:
	rstcheck -r "$(SOURCEDIR)"

html: 
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)"
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)."
