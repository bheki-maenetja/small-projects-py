def currency_formatter(num):
    # symbol = input("Enter your currency symbol: ")
    # while True:
    #     try:
    #         num = abs(float(input("Enter a number: ")))
    #         decimal_place = int(input("How many decimal places should your number be rounded to: "))
    #         num = round(num, decimal_place)
    #     except ValueError:
    #         print("Please a valid input!")
    #     else:
    #         break
    symbol, decimal_place = "$", 2
    integer, fraction = str(float(num)).split(".")
    while len(fraction) < decimal_place:
        fraction += "0"
    integer = [integer[i] for i in range(len(integer) - 1, -1, -1)]
    length = len(integer)
    for j in range(length):
        index = 4*j + 3 if 4*j + 3 < len(integer) else None
        if index == None: break
        integer.insert(index, ",")
    integer.reverse()
    format_num = symbol + "".join(integer) + f".{fraction}"
    return format_num

nums = list(map(currency_formatter, [120, 1230, 12340, 123450, 1234560, 12345670, 123456780, 1234567890, 12345678910, 123456789120]))
for i in nums:
    print(i)
