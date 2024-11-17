"""
Time Start: 3 38
Time End: 3 46

Notes:
Suggestion: for problems with more than one input we need a template.
ATM
"""

def main(x,y):

    if y < x or x % 5 != 0:
        return y

    return (y-x) - 0.5

def helper(string):
    nums = string.split(" ")

    return main(int(nums[0]),float(nums[1]))

numsInput = input()

print(helper(numsInput))