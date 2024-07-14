def super_func(*args,**kwargs):
    print(args)#tuple
    print(kwargs)#ditionary
    print(kwargs["num1"]+kwargs["num2"])
    return sum(args)+sum(kwargs.values())
print(super_func(1,2,3,4,num1=2,num2=10,num3=20))

#order rule: params, *args, default params, **kwargs
def func(param,*args,i="hi",**kwargs):
    print(args)#tuple
    print(kwargs)#ditionary
    print(kwargs["num1"]+kwargs["num2"])
    return sum(args)+sum(kwargs.values())
print(super_func(1,2,3,4,num1=2,num2=10,num3=20))

def f(*args,y,**kwargs):
    print(args)
    print(y)
    print(kwargs)


f(1, y=2, z=3)