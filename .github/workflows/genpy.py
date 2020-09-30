filepath = './.github/workflows/myfile2.txt'    
with open(filepath, "a+") as f:
    data = f.read()
    f.seek(0)
    f.write(output)
    f.truncate()    
