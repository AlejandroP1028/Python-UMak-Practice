"""
Time Start: 3 30
Time End: 3 37
Middle Character
"""

def main(inp):

    return inp[len(inp)//2] if len(inp) % 2 == 1 else f"{inp[len(inp)//2]}{inp[len(inp)//2 - 1]}"


print(main("hellos"))

