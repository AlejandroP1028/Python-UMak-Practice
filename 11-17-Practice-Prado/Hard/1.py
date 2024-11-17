"""
Time Start: 5 47
Time End: 6 26

Unique Subsequence
Notes:
need to work on String manip
"""

def main(s):
    maxSub = ""
    current = ""

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] != s[i + 1]:
            if len(current) > 0:
                current += s[i + 1]
            else:
                current = s[i] + s[i + 1]
        else:
            if len(current) > len(maxSub):
                maxSub = current
            current = ""


    if len(current) > len(maxSub):
        maxSub = current

    print(len(maxSub))


def helper():

    T = int(input())
    cases = []
    for i in range(0,T):
        holder = []
        tempN = int(input())
        tempS = input()
        holder.append(tempN)
        holder.append(tempS)
        cases.append(holder)

    for case in cases:
        print(case)
        main(case[1])


helper()