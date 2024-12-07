

listA=[]
listB=[]

with open('./day1/input.txt', 'r') as file:
    
    lists = file.readlines()

    for list in lists:
        list = list.strip()
        itemA, itemB = list.split('   ')
        listA.append(int(itemA))
        listB.append(int(itemB))



totalsimilarity = 0
for i in range(len(listA)):
    count = listB.count(listA[i])
    totalsimilarity += listA[i] * count


print(listA)
print(listB)

print(totalsimilarity)


    