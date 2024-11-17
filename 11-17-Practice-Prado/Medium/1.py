"""
Time Start: 3 51
Time End: 4 01

Notes:
We can use binary search in these kinds of problems.
Save Patients
"""

def main(N, vaccineStrength, mCount):
    l,r = 0,N-1

    while l < r:
        if int(vaccineStrength[l]) < int(mCount[l]) or int(vaccineStrength[r]) < int(mCount[r]):
            return "No"
        l += 1
        r -= 1

    return "Yes"


def helper():

    N = int(input())

    vaccineStrength = input().split(" ")

    mCount = input().split(" ")

    return main(N,vaccineStrength,mCount)


print(helper())