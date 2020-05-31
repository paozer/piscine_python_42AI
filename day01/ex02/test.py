from vector import Vector
import numpy as np

a = Vector([0, 1, 2, 3])
b = Vector([-2, 0, -0.5, 1])

print("base vectors")
print('a ' + repr(a))
print('b ' + repr(b))
print()

print('a + b =\t\t' + repr(a + b))
print('a + 3 =\t\t' + repr(a + 3))
print('a - b =\t\t' + repr(a - b))
print('a * b =\t\t' + repr(a * b))
print('a * 3 =\t\t' + repr(a * 3))
print('a / 3 =\t\t' + repr(a / 3))
print()

print('a rsub b =\t' + repr(a.__rsub__(b)))
print('3 * a =\t\t' + repr(3 * a))
print('3 / a =\t\t' + repr(3 / a))
print()

print('__str__ ' + str(a))
print('__repr__ ' + repr(a))


