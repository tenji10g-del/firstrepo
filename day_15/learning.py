zen= '''
beautiful is better that ugly.
explicit is better than inplicit.
simple is better that complex.
complex is better than complicated'''
for char in zen:
    if char not in "aeiou":
        print(char, end="")