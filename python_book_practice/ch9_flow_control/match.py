value = int(input("Enter a number: "))

match value:
    case 5 | 6:
        print("value is 5 or 6")
    case 7 | 8:
        print("value is 7 or 8")
    case 10 | 11 | 12 | 13 | 14 | 15:
        print("value between 10-15")
    case _:  # default case
        print("value is not 5, 6, 7, or 8")
