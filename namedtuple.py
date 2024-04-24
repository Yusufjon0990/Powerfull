from collections import namedtuple
"""
TATU = namedtuple("TATU", ["rektor", "dekan"])
T1 = TATU('Bobur', ['Alisher','Temur'])

print(T1.rektor)
print(T1.dekan)
T1.dekan.append('Kozim')
print(T1.dekan)
print(hash(TATU))
"""


"""
autocity = namedtuple('autocity',['name','price','color',])
X1 =autocity('BMW', '25000$', ['black','white','blue'])
X2 = autocity('Mers', '30000$', ['black','white','blue'])
X3 = autocity('gm.gentra', '18000$',['black','white','blue'])
print(X1.name)
print(X2.price)
print(X3.color)
autocity.color = (['derk blue'])
print(autocity.color)
"""

"""
person = namedtuple('person',['name','age','year','height'])
p1 = person(['Jack'],25,1999,1.80)
p2 = person(['Mike'],30,1995,1.68)
p3 = person(['Alisher'],21,2003,1.70)
print(p1.name)
print(p2.age)
p1.name.append('Jasur')
print(p1.name)
print(p3.height)
"""
"""
Car = namedtuple('Car', ['model', 'color', 'year'])

db = {'model': 'BMW', 'color': 'black', 'year': 2024}
print(Car(**db))
"""
"""
point = namedtuple('point', ['x', 'y'])
p1 = point(2,5)
print(p1.x)
print(p1.y)
point.x = 8
print(point.x)
"""
