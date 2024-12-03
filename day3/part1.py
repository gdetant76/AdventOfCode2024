
import re
























with open('./day3/input.txt', 'r') as file:
    reports = file.readlines()
    
    sum=0

    for line in reports:
        line = line.strip()
        pattern = r"mul\(\d+,\d+\)"

        match = re.findall(pattern, line)

        
        for item in match:
            numbers = re.findall("\d+",item)
            multi = int(numbers[0]) * int(numbers[1])
            sum += multi

    print(sum) 
    
    