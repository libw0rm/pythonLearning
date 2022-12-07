''' Q[001]
a = [0, 1, 0]
b = [1, 1, 0]
s = 0

for x in (a,b,a):
    s += x.count(1)

print(s)
# '''

''' Q[002]
a = (0, 1, 2, 3, 4, 5)
b = slice(0, 2)
print(a[b])
# '''

''' Q[003]
def f1():
    x = 100
    print(x)
x = + 1
f1()
# '''

''' Q[004]
a = {3, 4, 5}
a.update([1, 2, 3])
print(a)
# '''

# '''Q[005]
def foo(x):
    x = ['def', 'abc']
    return (x) and id(x)

q =['123', '456']
z = foo([0][0])

# check id for everythink
print('id @foo:', id(foo))
print('id @foo(q):', id(foo(q)))
print('id @foo(z):', id(foo(z)))
print('id @(q):', id(q), '<-', q)
print('id @(z):', id(z), '<-', z)
print('id @(q[0]):', id(q[0]),'<-', (q[0]))
print('id @(q[1]):', id(q[1]),'<-', (q[1]))
print('id @(q[1][0]-4):', id(q[1][0]), '<-', q[1][0])
print('id @(q[1][1]-5):', id(q[1][1]), '<-', q[1][1])
print('id @(q[1][2]-6):', id(q[1][2]), '<-', q[1][2])
print('id @foo(x[0][0]-d):', id(foo([0][0])), '<-', z, '<->', foo([0][0]))
# '''


