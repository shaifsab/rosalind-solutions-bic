def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol


def number_to_symbol(number):
    if number == 0:
        return "A"
    elif number == 1:
        return "C"
    elif number == 2:
        return "G"
    elif number == 3:
        return "T"


number = int(input("Enter an integer: "))
k = int(input("Enter the length of the DNA string: "))
pattern = number_to_pattern(number, k)
print(pattern)