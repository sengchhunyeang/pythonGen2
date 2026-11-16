day = int(input("day :"))

# if day = 1 and day = 2 
match day:
    case 1 | 2|3|4|5:
        print("work day")
    case 6|7 :
        print("Weekend day ")
    case _:
        print("Unknown")