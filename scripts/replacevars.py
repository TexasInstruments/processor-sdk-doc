# write_replacevars
# -----------------
# Description:  Writes replacement variable array to source/${OS}/replacevars.rst.inc
#
# Parameters: app          - Application calling this Python function
#             replacevars  - Input hash table of replacevars that will be converted into
#                            "replace" directives in the replacevars.rst.inc file

def unpack_replacevars(replacevars):
    replacevarstext = ["\n"]
    for key, val in replacevars.items():
        if val == "\\":
            replacevarstext.append(f".. |{key}| unicode:: U+00000\n")
        else:
            replacevarstext.append(f".. |{key}| replace:: {val}\n")
    replacevarstext.append("\n")
    return ''.join(replacevarstext)
