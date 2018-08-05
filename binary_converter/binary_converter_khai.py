def binary_to_decimal(bin_num):
    # Turn bin_num to str
    bin_str = str(bin_num)

    # Reverse string
    bin_str = bin_str[::-1]

    # Loop on each digit in the binary string and multiplicate it by the power of 2 it represents
    # and add it to total
    total = 0
    for i in range(len(bin_str)):
        total += ((2**i) * int(bin_str[i]))

    print (total)


def decimal_to_binary(dec_num):
    # Base case: If number is 0, return 0
    if dec_num == 0:
        return 0

    # Initial empty string to hold binary value
    bin_str = ''

    # Loop till number = 0
    while dec_num > 0:
        remainder = dec_num % 2
        bin_str = str(remainder) + bin_str

        # Divide dec_num by 2
        dec_num //= 2

    print (int(bin_str))


binary_to_decimal (11)
decimal_to_binary (3)
