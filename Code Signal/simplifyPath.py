def simplifyPath(path):
    splitted = path.split('/')
    print(splitted)
    output = []
    for item in splitted:
        if item == "" or item ==".":
            continue
        elif item == "..":
            if len(output) != 0 :
                output.pop(len(output) - 1)
        else:
            output.append(item)
    return '/' + '/'.join(output)
