import re






with open('./day3/input.txt', 'r') as file:
    reports = file.readlines()
    
    matchespos = set()


    pattern = r"mul\(\d+,\d+\)"
    
    for line in reports:
        line = line.strip()
        matches = re.finditer(pattern, line)

        for match in matches:
            matchespos.add(match)
            print(match)

