# Contributing to processor-sdk-doc

## Commit formatting

The main requirements are that commits contain a reasonable commit message and
are correctly Signed-Off-By you, the contributor, prior to opening a PR.

Most commit subjects contain the name of the file being modified, but this is
not strictly enforced.

Please see the following for additional resources on commit formatting:
https://www.conventionalcommits.org/en/v1.0.0/

### Commit types

Each commit has a tag with its type following the conventional commit
convention. The following goes over the more common tags in this project.

 - `feat`: any *addition* to the RST sources or platform configs
 - `fix`: any *correction* to the RST sources or platform configs
 - `style`: any modification that does not change the meaning of the source
 - `refactor`: any modification that neither add a feature or fixes the source
 - `build`: changes that affect the build system, container, or external
   dependencies
 - `ci`: changes to the CI pipelines or associated scripts
 - `docs`: changes to *project* documentation, such as the main README

 Other supported tags exist in the conventional commit specification, but they
 are not used as often here.

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

Other directories contain sphinx specific overrides that help convert the above
resources into the standard HTML release.

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
newline that separates the directive from the content block:

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
platform configs, or reported during the build in the `rst_prolog` section.

### Ifconfigs

The way we handle multiple platform sections without a lot of duplication is by
conditionally dropping sections that do not match the active platform. This is
achieved through the use of the [ifconfig
directive](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html).
Not all parsers will respect this directive, so be sure to try compiling the
documentation for a platform that matches the ifconfig prior to submitting a PR.

#### Behavior

You cannot use the ifconfig directive to avoid parsing other directives,
sections, or other RST components. The ifconfig directive acts as a standard RST
directive where content under it is conditionally masked in the final document
output.

Sphinx functionally has 2 main processing steps. The first path takes care of
substitutions, role and directive definitions, sections, and references. The
second pass actually processes the directives and other RST structures. Because
of this, RST underneath an ifconfig will be evaluated whether or not it visible
in the final document output.

In some cases, this can change the behavior of external components if they are
handled by the first processing step. For example, given the following snippet:

```rst
.. ifconfig:: CONFIG_part_variant in ('J721S2')

   Content

   .. |REPLACE_A| replace:: replace_b

|REPLACE_A|
```

When `CONFIG_part_variant` is `J721S2` you may correctly expect the following to
be rendered:

```
Content
replace_b
```

The disconnect comes in when `CONFIG_part_variant` is `J784S4`. The replacement
will still be defined and included into the main state machine that handles
refs, replacements, and other key directives regardless of whether the content
is displayed in the final document output. The following is the output generated
in this case:

```
replace_b
```

## Licensing

### Community

Scripts and other code-specific additions should be licensed as
[MIT](https://spdx.org/licenses/MIT.html) using the [SPDX short
identifiers](https://spdx.dev/learn/handling-license-info/) at the top of the
file as appropriate.

Other additions or modifications should be under
[CC-BY-SA-4.0](https://spdx.org/licenses/CC-BY-SA-4.0.html). See
[LICENSE](LICENSE) file for specific details.

### TI Employees

In addition to the community guidelines, Texas Instruments employees are
expected to assign licenses to TI as in the example below:

```text
SPDX-License-Identifier: MIT
Copyright (C) 2024 Texas Instruments Incorporated - https://www.ti.com
```

All other files inherit the generic CC-BY-SA-4.0 license and do not require an
explicit license / copyright notice.

## Vale grammar, spelling and prose checking

This project currently uses [Vale](https://vale.sh/) for grammar spelling and
prose checking. We operate on a loose version of [Red Hat's documentation style
guidelines](https://github.com/redhat-documentation/vale-at-red-hat).

If there are words it detects as misspellings, add those words to the custom
vocabulary entry in
[accept.txt](.github/styles/config/vocabularies/PSDK/accept.txt). If there are
words you see that you think do not constitute usage here, add those words to
the [reject.txt](.github/styles/config/vocabularies/PSDK/reject.txt). Ensure the
contents of these files are alphabetically sorted after any modifications.

Information about the formatting of these files is available
[upstream](https://vale.sh/docs/keys/vocab#file-format).

## Fighting workflows

The workflows are here to help, but occasionally they can raise false positives.
In such an event, please ping a reviewer and explain why the failure should be
ignored.

An example of this is adding new workflows. GitHub will attempt to execute these
workflows, but sometimes the source repo will be missing the required
components. In these cases it results in a failure that should be ignored.

Another case is when using certain replacement variables. Certain replacement
variables are only populated on some platforms, and only when a platform is
selected right now. Hopefully change in the future, but if this causes a
workflow failure right now it can be safely ignored.
