# demo.py

print("Hello VS Code")

for i in range(5):
    print(i)

a={1,2,3,4}
b={3,4,4,5}
print(a.union(b))

print(a.intersection(b))
print(a.difference(b))

def calc(a,b):
    return a+b,a*b

result = calc(3,4)
print(result)

args =(5,6)
print(calc(*args))

colors={"apple":"red","banana":"yellow"}
print(type(colors))

for item in colors.items():
    print(item)