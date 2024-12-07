

def CheckInc(report):
    i=0
    faults = 0
    safe = True
    while i < len(report)-1 and faults<2:
        j=i+1
        if not(report[i]<report[j] and report[i] >= report[j]-3):
            if j==len(report)-1:
                faults+=1
                break
            j=j+1
            if report[i]<report[j] and report[i] >= report[j]-3:
                faults+=1
                i=i+2
            else:
                if i==0:
                    faults+=1
                    i += 1
                else:
                    
                    i=i-1
                    j=j-1
                    if report[i]<report[j] and report[i] >= report[j]-3:
                        faults+=1
                        j=j+1
                        i=i+2
                    else:
                        safe = False
                        break
        else:
            i=i+1
    

    return safe and faults < 2

def CheckDec(report):
    i=0
    faults = 0
    safe = True
    while i < len(report)-1 and faults<2:
        j=i+1
        if not(report[i]>report[j] and report[i] <= report[j]+3):
            if j==len(report)-1:
                faults+=1
                break

            j=j+1
            
            if  report[i]>report[j] and report[i] <= report[j]+3:
                faults+=1
                i=i+2
            else:
                if i==0:
                    faults+=1
                    i += 1
                else:
                    i=i-1
                    j=j-1
                    if report[i]>report[j] and report[i] <= report[j]+3:
                        faults+=1
                        j=j+1
                        i=i+2
                    else:
                        safe = False
                        break
        else:
            i=i+1

    return safe and faults < 2




with open('./day2/input.txt', 'r') as file:
    
    reports = file.readlines()
    totalsafe = 0
    for list in reports:
        list = list.strip()
        items = list.split(' ')
        report = [int(item) for item in items]
        faultsInc = 0
        faultsDec = 0       
       # print("Inc: ", CheckInc(report), "Dec :",CheckDec(report))

        if CheckInc(report) or CheckDec(report):
            totalsafe += 1
        else:
            print(report)

    print(totalsafe)


        
#        for i in range(len(report)):
 
#           j=i+1
#            if not(report[i]<report[j] and report[i] >= report[j]-3):
#                
#
#
#        for i,j in zip(report, report[1:]):
#            if not(i < j and i >= j-3):
#                faultsInc +=1
#           if not(i > j and i <= j+3):
 
#                faultsDec +=1 
#        if faultsInc <= 1 or faultsDec <=1:
#            lineSafe = True

#        print("faultInc:",faultsInc,"faultDec:",faultsDec, "Safeline:",lineSafe)
        
        
#    print(totalsafe)


#res = all((i < j and i > j-1) for i, j in zip(test_list, test_list[1:]))
#integer_list = [int(item) for item in string_list]