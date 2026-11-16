students = [
    {"id": 1, "name": "Dara", "age": 20, "gender": "Male", "score": 85},
    {"id": 2, "name": "Sokha", "age": 21, "gender": "Female", "score": 90},
    {"id": 3, "name": "Vanna", "age": 19, "gender": "Male", "score": 75},
    {"id": 4, "name": "Sreymom", "age": 22, "gender": "Female", "score": 95},
    {"id": 5, "name": "Bopha", "age": 20, "gender": "Female", "score": 80},
    {"id": 6, "name": "Rith", "age": 23, "gender": "Male", "score": 65},
    {"id": 7, "name": "Sokun", "age": 21, "gender": "Male", "score": 88},
    {"id": 8, "name": "Chantha", "age": 19, "gender": "Female", "score": 92},
    {"id": 9, "name": "Pisey", "age": 20, "gender": "Female", "score": 78},
    {"id": 10, "name": "Vicheka", "age": 22, "gender": "Male", "score": 84},
    {"id": 11, "name": "Malis", "age": 18, "gender": "Female", "score": 96},
    {"id": 12, "name": "Sovann", "age": 24, "gender": "Male", "score": 70},
    {"id": 13, "name": "Kanha", "age": 21, "gender": "Female", "score": 89},
    {"id": 14, "name": "Borey", "age": 20, "gender": "Male", "score": 76},
    {"id": 15, "name": "Dalin", "age": 19, "gender": "Female", "score": 93}
]

# Homework 3 ( use option condition )
# 1 - use for loop for loop through data from list (list of dictionary)
# 2 - list only Female
# loop
while True:
    print("1 : show all student ")
    print("2 : show only student Female ")
    user_input = int(input("entry :  "))  # VALUE default string
    print(type(user_input))
    if user_input == "1":
        for i in students:
            print(i)
    elif user_input == "2":
        for i in students:
            if i["gender"] == "Female":
                print(i)
