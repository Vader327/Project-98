file1_name = input("Enter the name of the first file: ")
file2_name = input("Enter the name of the second file: ")

file1 = open(file1_name, "r")
data1 = file1.read()
file1.close()

file2 = open(file2_name, "r")
data2 = file2.read()
file2.close()

file1 = open(file1_name, "w")
file1.write(data2)
file1.close()

file2 = open(file2_name, "w")
file2.write(data1)
file2.close()

