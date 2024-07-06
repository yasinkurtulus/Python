def outer_function(a, b):
    str="dfdsf"
    def inner_function(c, d):
        print(str)
        sdf="sdfsd"
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)