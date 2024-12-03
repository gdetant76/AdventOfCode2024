import re


def FindNextDo(line, pos):
    patterndo = r"do\(\)"

    matches = re.finditer(patterndo, line)

    for match in matches:
            if match.start() > pos:
                 return match.end()
    return -1

    
def CalculateLine(line):
    pattern = r"mul\(\d+,\d+\)"

    sum = 0
    match = re.findall(pattern, line)
      
    for item in match:
        numbers = re.findall("\d+",item)
        multi = int(numbers[0]) * int(numbers[1])
        sum += multi
    return sum


with open('./day3/input.txt', 'r') as file:
    reports = file.readlines()
    
    sum=0

    pattern = r"mul\(\d+,\d+\)"
    patterndont = r"don't\(\)"
    
    startwithDont = False
    
    giantline = ""
    for line in reports:
        giantline += line.strip()

    match = re.search(patterndont, giantline)

    while match is not None:
        pos = FindNextDo(giantline, match.start())
        print("location dont: ", match.start(), "location do:", pos)
        giantline = giantline[:match.start()] + giantline[pos:]
        match = re.search(patterndont, giantline) 

    sum = CalculateLine(giantline)
    
    print(sum)
    

    
 #   for line in reports:
 #       line = line.strip()
 #       lineMul = ""
#
#        if startwithDont:
 #          match = re.search("!", line) 
 #          startwithDont = False
 #       else:
 #           match = re.search(patterndont, line)
 #       while match is not None:
 #           pos = FindNextDo(line, match.start())
 #           print("location dont: ", match.start(), "location do:", pos)

 #           if pos == -1:
 #                line = line[:match.start()]
 #                startwithDont = True
 #           line = line[:match.start()] + line[pos:]
 #           match = re.search(patterndont, line) 
#
 #       sum += CalculateLine(line)
        
  #      print(line)
  #      print(sum)
  #      print(' ')
    
  #  print(sum)




