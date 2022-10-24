#


matrix=[['00','01','02','03','04','05'],['10','11','12','13','14','15'],['20','21','22','23','24','25'],['30','31','32','33','34','35']]

print(matrix)
print('_______________________')
print(f"matrix[2][3]= {matrix[2][3]}")
print('_______________________')
for i in matrix:
    print(i)
print('_______________________')
for i in matrix:
    for k in i:
        print(k)
print('_______________________')
for i in matrix:
    for k in i:
##        if matrix.index(k)==1:
##            print(k)
##        print(matrix.index(i))
        print(i.index(k))
print('___________=____________')
print(f"matrix[2]= {matrix[2]}")
print('_______________________')

#print(f"Name: {name}, age: {age}")
