# What will be printed

x = 5

def outer():
    x = 10
    def inner():
        print(x)       
    inner()
outer()

