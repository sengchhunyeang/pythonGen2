# *args
# function building
def sum_value_multiple(*anc):
    return sum(anc)


valueA = sum_value_multiple(2, 4)
print(valueA)


def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


show(name="Lymeng", age=18,address="PP",testing = "Testing")
