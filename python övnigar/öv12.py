def food(s, vegan=False):

    if vegan == True:
        return"sojamjölk"
    else:
        return"mjölk"

print(food("mjölk"))       # mjölk
print(food("mjölk", True)) # sojamjölk
