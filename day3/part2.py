import re






with open('./day3/input.txt', 'r') as file:
    reports = file.readlines()
    
    matchespos = set()


    pattern = r"mul\(\d+,\d+\)"
    patterndont = r"don't\(\)"

    
    for line in reports:
        line = line.strip()
        matches = re.finditer(pattern, line)

        for match in matches:
            matchespos.add(match)
            print(match)

