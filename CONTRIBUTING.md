# Contributing to processor-sdk-doc

## Commit formatting

The main requirements are that commits contain a reasonable commit message and
are correctly Signed-Off-By you, the contributor, prior to opening a PR.

Most commit subjects contain the name of the file being modified, but this is
not strictly enforced.

Please see the following for additional resources on commit formatting:
https://www.conventionalcommits.org/en/v1.0.0/

## Project structure

This project uses reStructuredText (reST or RST) for generating standard HTML
from the given source files and configs. For more information on how to get
started with reStructuredText, see:

 - https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
 - https://docutils.sourceforge.io/docs/index.html

RST source files and other build assets are listed under the `source/`
directory.

Build configuration files that hold platform specific variables are under the
`configs/` directory.

Scripts to verify source files and generally lint the documents are under the
`bin/` directory.

The container build tools are listed under the `docker/` directory.

Other directories contain sphinx specific overrides that help massage the above
resources into the standard documentation HTML release.

## Adding new dependencies

Though we try to keep build dependencies to a minimum, occasionally this is
necessary. In such occasions, build dependencies should be adjusted in the
`requirements.txt` file in a commit preceding the introduction of the code that
depends on that package.

For example, if you wish to add a section to the document that uses sphinx-tabs
and sphinx-tabs is not already in the `requirements.txt` file, add it to the
file and commit that change before adding the desired section.

This keeps the repository reasonably bisectable.

## RST Styling

We are trying to migrate sections over to
[rstcheck](https://github.com/rstcheck/rstcheck) style formatting, but this is a
slow process. There is a workflow to make sure there are no regressions, but
updating older sections is appreciated.

### Include files

RST files intended to be included should be prepended with an underscore, like
`_Boot_Monitor.rst`. This indicates that the file should not be indexed but
allows parsers and text editors to still pick up the expected format.

### Indentation and whitespace

RST is very whitespace focused. 3 spaces is the current standard. This allows
code sections to clearly line up with directive:

```rst
.. code-block:: console

   abc@641cd7b33c02:/build$ ls

```

Make sure that the directive and the content block have 1 new line between them
and that the content block has at least 1 newline after it.

Directives that take parameters should place their parameters prior to the
newline that seperates the directive from the content block:

```
.. figure:: /images/buildroot_menuconfig.png
   :height: 600
   :width: 800

   Buildroot Menuconfig

```

### Variable usage

There are a number of predefined variables available that are dynamically set
based on the platform config. These variables should be used wherever possible.
These variables can be found in the "Replacement Variables" section of the
platform configs, or in the temporary file placed at `source/_replacevars.rst`
during the build process.

### Ifconfigs

The way we handle multiple platform sections without a lot of duplication is by
conditionally dropping sections that do not match the active platform. This is
acheived through the the use of the [ifconfig
directive](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html).
Not all parsers will respect this directive, so be sure to try compiling the
documentation for a platform that matches the ifconfig prior to submitting a PR.

## Fighting workflows

The workflows are here to help, but occasionally they can raise false positives.
In such an event, please ping a reviewer and explain why the failure should be
ignored.
