f= open("./.github/workflows/myfile2.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
