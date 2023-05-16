string = input("Enter a genome string: ")


skew = [0]


for i in range(len(string)):
    if string[i] == 'C':
        skew.append(skew[-1] - 1)
    elif string[i] == 'G':
        skew.append(skew[-1] + 1)
    else:
        skew.append(skew[-1])


min_skew = min(skew)


positions = [i for i in range(len(skew)) if skew[i] == min_skew]


print(positions)