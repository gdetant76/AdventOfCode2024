
def GetMiddlepageNumber(updatelist):

    if len(updatelist) % 2 ==0:
        print("oo")   
    middlepage = int(len(updatelist)/2)
    return int(updatelist[middlepage])





with open('./day5/input.txt', 'r') as file:
    reports = file.readlines()

    UpdateSequenceset = set()

    ReadingUpdateSequence = True

    sum = 0
    for line in reports:
        line = line.strip()
        if line == "":
            ReadingUpdateSequence = False
        else:
            if ReadingUpdateSequence:
                i,j = line.split('|')
                UpdateSequenceset.add((int(i),int(j)))
            else:
                Updatelist = line.split(',')
                Updatelist.reverse()

                rightinorder = True
                for i in range(len(Updatelist)-1):
                    for j in range(i+1,len(Updatelist)):
                       
                        if (int(Updatelist[i]),int(Updatelist[j])) in UpdateSequenceset:
                            rightinorder = False
                if rightinorder:
                    Updatelist.reverse()
                    sum += GetMiddlepageNumber(Updatelist)
                    
                    print("right in order",Updatelist)
    print(sum)
                        
                    
                


