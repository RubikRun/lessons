def readfile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return [char for char in content if char in ('O', '-')]



count = 0

for x in range(10):
    flist = readfile( str(x) + ".txt")
    for y in range( len(flist) ):
        if flist[y] == 'O':
            count += 1

print(count)