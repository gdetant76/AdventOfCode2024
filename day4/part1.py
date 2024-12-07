import re
from tokenize import group

def XMAShorizontal(reports):
    sum = 0
    for line in reports:
        line = line.strip()

        matches = line.count("XMAS")
        matches += line.count("SAMX")

        sum += matches

    return sum

def XMASDiagonal(reports):
    sum = 0
    strings = [] 
    for i in range(len(reports)-3):
        for j in range(len(reports[i])-4):
            if reports[i][j] == 'X':
                if reports[i+1][j+1] == 'M':
                    if reports[i+2][j+2] == 'A':
                        if reports[i+3][j+3] == 'S':
                            sum += 1

    for i in range(len(reports)-3):
        for j in range(len(reports[i])-4):
            if reports[i][j] == 'S':
                if reports[i+1][j+1] == 'A':
                    if reports[i+2][j+2] == 'M':
                        if reports[i+3][j+3] == 'X':
                            sum += 1
    
    
    return sum

def XMASRevDiagonal(reports):
    sum = 0
    strings = [] 
    for i in range(len(reports)-3):
        for j in range(3,len(reports[i])-1):
            if reports[i][j] == 'X':
                if reports[i+1][j-1] == 'M':
                    if reports[i+2][j-2] == 'A':
                        if reports[i+3][j-3] == 'S':
                            sum += 1

    for i in range(len(reports)-3):
        for j in range(3,len(reports[i])-1):
            if reports[i][j] == 'S':
                if reports[i+1][j-1] == 'A':
                    if reports[i+2][j-2] == 'M':
                        if reports[i+3][j-3] == 'X':
                            sum += 1
    
    
    return sum

with open('./day4/input.txt', 'r') as file:
    reports = file.readlines()
    
    sum = XMAShorizontal(reports)
    
    
    transposed = [''.join(chars) for chars in zip(*reports)]
    sum += XMAShorizontal(transposed)

    sum += XMASDiagonal(reports)
    sum += XMASRevDiagonal(reports)
    
    print(sum)