
import re

def FindMASdiag(reports,i, j):
    if reports[i][j] == 'M':
        if reports[i+1][j+1] == 'A':
            if reports[i+2][j+2] == 'S':
                        return True
    if reports[i][j] == 'S':
        if reports[i+1][j+1] == 'A':
            if reports[i+2][j+2] == 'M':
                        return True
    return False

def FindMASRevdiag(reports,i, j):
    if reports[i][j+2] == 'M':
        if reports[i+1][j+1] == 'A':
            if reports[i+2][j] == 'S':
                        return True
    if reports[i][j+2] == 'S':
        if reports[i+1][j+1] == 'A':
            if reports[i+2][j] == 'M':
                        return True
    return False


def FindXMAS(reports):
    sum = 0
    strings = [] 
    for i in range(len(reports)-2):
        for j in range(len(reports[i])-3):
            if FindMASdiag(reports,i,j):
                 if FindMASRevdiag(reports,i,j):
                      sum += 1
    
    return sum

with open('./day4/input.txt', 'r') as file:
    reports = file.readlines()
    
    sum = FindXMAS(reports)
    

    
    print(sum)


