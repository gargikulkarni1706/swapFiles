def swapFileData():
    fileNameOne= input("Enter the name of the first file.")
    fileNameTwo= input("Enter the name of the second file.")
    with open(fileNameOne, "r") as a:
     data_a= a.read()
    with open(fileNameTwo, "r") as b:
     data_b= b.read()
    with open(fileNameOne, "w") as a:
     a.write(data_b)
    with open(fileNameTwo, "w") as b:
     b.write(data_a)
swapFileData()