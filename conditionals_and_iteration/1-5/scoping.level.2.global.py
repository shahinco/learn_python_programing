def outer():
    test = 1 # Outer scope

    def inner():
        global test
        test = 2 # global scope
        print('inner:', test)

    inner()
    print('outer:', test)

test = 0 # global scoper
outer()
print('global: ', test)