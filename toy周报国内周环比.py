#!/usr/bin/env python3

import sys

def get_input():
    print("input numbers")
    blank = False
    lines = []
    while True:
        line = sys.stdin.readline().strip()
        if len(line) < 2:
            if blank:
                break
            else:
                blank = True
        else:
            blank = False
            s = list(filter(lambda ch: ch in '0123456789.', line))
            lines.append(float(''.join(s)))
    return lines

def main():
    lines_1 = get_input()
    lines_2 = get_input()
    lines_3 = []
    for i in range(len(lines_1)):
        n = (lines_2[i] - lines_1[i])/lines_1[i]
        n = round(n*100, 2)
        lines_3.append(n)
    #print(lines_1)
    #print(lines_2)
    #print(lines_3)
    for i in lines_3:
        print(str(i)+"%")
    return

if __name__ == '__main__':
    main()
