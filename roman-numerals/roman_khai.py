from collections import  OrderedDict


# 4000 -> MMMM
#
# Step 1: divide by 1000
#  quotient 4, remainder 0
#  'M' * 4
# 150 -> C +  L
#
# Step 1: divide by 100
#  quotient 1, Remainer 50
# Step 2: divide by 50
#  quotient 1, Remainer 0
#
# look for closest literal equal or less than given number
# 1000, remaining 3000 : if key <= number:
# 1000, remaining 2000 : if key <= number
# 1000, remaining 1000
# 1000, remaining 0
#
# 5/2 => qu: 2, remainder 1

def decimal_to_roman(decimal_number):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def decimal_to_roman(decimal_number):
        for divisor in roman.keys():
            quotient, remainder = divmod(decimal_number, divisor)
            # 4, 300
            # 3, 0

            if quotient > 0:
                yield roman[divisor] * quotient
                # yield "MMMM"
                # yield "CCC"

            decimal_number = remainder # set to remainder for next iteration.
            # decimal_number = 300
            # decimal_number = 0

            if remainder > 0:
                decimal_to_roman(remainder)
            else:
                break

    return "".join(decimal_to_roman(decimal_number))

#CIX -> 100 + 9

# CIX
# C, CI: 100, -1 -> 100
# move to next char
# I, IX: 1, 9 -> 9

# CDXCVII
# C, CD: 100, 400 -> 400
# move to next 2 char
# X, XC: 10, 90 -> 90
# move to next 2 char
# V, VI: 5, -1 -> 5
# move to next char
# I, II: 1, -1 -> 1
# move to next char
# I:  1 -> 1
# 497


# check if single letter in dictionary
# and also check for double letter in dictionary


def roman_to_decimal(roman_number):
    def to_arabic(roman_number):
        decimal = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'Xl': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        # LXX
        if len(roman_number) == 0: #base case
            return 0

        first_literal = roman_number[0]
        second_literal = None

        if len(roman_number) > 1: # there is a second character following first_literal
            second_literal = roman_number[:2]
        first_number, second_number = (
            decimal.get(first_literal, -1),
            decimal.get(second_literal, -1),
        )

        number = max(first_number, second_number)

        if number == first_number:
            # step one character ahead
            return number + to_arabic(roman_number[1:])
            # 50 + to_arabic("XX")
            # 50 + 10 + to_arabic("X")
            # 50 + 10 + 10 + to_arablic("")
        else:
            # step two characters ahead
            return number + to_arabic(roman_number[2:])

    return to_arabic(roman_number)

def main():
    """
    Add custom tests here.
    """
    user=int(input('enter a number:'))

if __name__ == '__main__':
    main()