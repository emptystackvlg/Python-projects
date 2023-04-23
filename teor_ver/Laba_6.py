mass = []
with open('C:\\Users\\Alexandr\\Documents\\GitHub\\Python-projects\\teor_ver\\file.txt',"r") as file:
    lines = file.readlines()
    for line in lines: 
        read_line = [float(x) for x in line.split()]
        mass.append(read_line)
    for i in range (len(mass)):
        print ("i = " + str(i))
        for j in mass[i] :
            print (j)