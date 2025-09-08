# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y:
        return x
    else:
        return y


"""maximo2 = max_of_two(int(input()),int(input()))
print(maximo2)"""

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if (x > y) and (x > z):
        return x
    if (y > x) and (y > z):
        return y
    return z

maximo3 = max_of_three(int(input()),int(input()),int(input()))
print(maximo3)    

