


# ask how many row
row=int(input("How many rows: ")) 


# ask how many cols
col=int(input("how many columns: "))

Eid_list=[]

for i in range(row):
    rowList=[]
    for m in range(col):
        rowList.append("❤️ ")
    Eid_list.append(rowList)

for i in range(row):
    for j in range(col):
        print(Eid_list[i][j],end=" ")
    print()