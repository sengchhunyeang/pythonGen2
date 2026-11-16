def backup():
    return 2


def backup1(a, b):
    result = a + b
    # print(value)


valueA = backup()
result = valueA + 5
# print(result+1+1)
result_func = backup1(2, 5)
print(result_func)


def refund(cost):
    nodule = 800
    return cost - nodule # remail 1200
def refund_tech(cost):
    pencil =500 #1200-500 = 700
    return cost-pencil

getter = refund(2000)

print("get refund :",getter)

print(refund_tech(getter))