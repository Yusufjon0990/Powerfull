from decimal import Decimal, getcontext , Context

print(Decimal(0.2) + Decimal(0.3) == Decimal(0.5))

getcontext.Prec = 6
a = Decimal(0.1) + Decimal(0.2)
b = Decimal(0.3)

#print(float(a) == float(b))



new_context = Context(prec=2, rounding  = Decimal.round_up)
Decimal.setcontext(new_context)
getcontext().traps[Decimal.divisionByzero] = False


print(Decimal(5) / Decimal(0))

x = 1.422245
y = 2.542245
print(x + y)

print(0.2 + 0.2 + 0.2)

from decimal import Decimal

result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(type(result))

number = Decimal("0.1")
number = number + 4
print(type(number), number)
from decimal import getcontext

getcontext().prec = 3
result =  Decimal(1) / Decimal(7)
print(result)
pi = 3.145353645523
print(pi)
print(1/7)
r = 1
pi = Decimal('3.1451231243')
s = pi*r*r
print(s)

from math import ceil, floor

print(floor(5.999999999999999)) # -> o'zidan kichik songa (chap tomonga) yaxlitlaydi
print(ceil(5.0000000000001)) # ->  o'zidan katta songa (o'ng tomonga) yaxlitlaydi
print(round(11.5))

from decimal import Decimal


number = Decimal("10.447")
number = number.quantize(Decimal("0.00"))
print(number)


from decimal import Decimal, ROUND_HALF_EVEN

number = Decimal("10.025")  # 2 - ближайшее четное число
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))  # 10.02

number = Decimal("10.085")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))




