i = 28
print(f"I am {i} years old")

for n in range(2):
    print (n)

s = set()

def square(x):
    return x * x

for i in range(10):
    print("{} squared is {}".format(i,square(i)))

class Point:
    def _init_(self,x,y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)
