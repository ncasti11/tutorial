def to_the_power(x, y = 2):
    result = x
    for i in range(0, y):
        result = result * x
    return result

x = 150
y = 2
print("{0} to the power of {1} is: {2}".format(x, y, to_the_power(x, y)))
