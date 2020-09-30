filepath = './.github/workflows/myfile2.txt'
with open(filepath, 'a+') as fp:
    line = fp.readline()
    print(line)
