numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def int_2_roman(value):
    if value > 3999 or value < 1:
        print("Invalid roman number")
    numeral = list()
    i = 0
    while value > 0:
        if value - values[i] >= 0:
            numeral.append(numerals[i])
            value -= values[i]
        else:
            i+=1
    return ''.join(numeral)

print(int_2_roman(94))