nbr_pieces = input("Ange input: ")
correct_set = [1,1,2,2,2,8]
y = 0
output=""
for x in nbr_pieces:
    dif = correct_set[y]-int(x)
    output+=str(dif)
    y+=1
print(int(output))
