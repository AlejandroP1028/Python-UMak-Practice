"""
Time Start: 5 20
Time End: 5 27


Pentagonal numbers
Notes:

    Can be useful for number pattern questions
    -- Quadratic Equation =
         Pn = an^2 + bn + c

         Steps =
         1. Eliminate C
         2. Find a and b
         3. Find c by using a and b in the first equation
         4. plug in a,b, and c in the base formula
         5. Simplify and we get the formula for pentagonal number.s



"""
def main():
    for i in range(0, 50):

        num = i + 1
        print(f"{i+1}:{(num * (3 * num - 1) // 2)} ")

print(main())