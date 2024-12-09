# unpack_replacevars
# -----------------
# Description: Creates a valid RST replacement variable list from the given variable dictionary
#
# Parameters: replacevars  - Input hash table of replacevars that will be converted into
#                            "replace" directives

def unpack_replacevars(replacevars):
    replacevarstext = ["\n"]
    for key, val in replacevars.items():
        if val == "\\":
            replacevarstext.append(f".. |{key}| unicode:: U+00000\n")
        else:
            replacevarstext.append(f".. |{key}| replace:: {val}\n")
    replacevarstext.append("\n")
    return ''.join(replacevarstext)
