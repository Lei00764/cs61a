def make_adder(x):
    def adder(y):
        return x + y
    return adder

print(make_adder(1)(3))

# 或者这样看：
f = make_adder(1)
print(f(3))