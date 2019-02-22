numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def integer_to_roman(value):
    numeral = str()
    i = 0
    while value > 0:
        if value - values[i] >= 0:
            # numeral.append(numerals[i])
            numeral = ''.join(numerals[i])
            value -= values[i]
        else:
            i += 1
    return print(numeral)

integer_to_roman(95)