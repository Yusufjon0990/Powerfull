# fibonachi whileda
# n = 20
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1
#
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()

class Fibonacci:
    def __init__(self, stop):
        self._current = 0
        self._stop = stop
        self._index = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fibo_number = self._current
            self._current, self._next = self._next, self._current + self._next

            return fibo_number
        else:
            raise StopIteration


fibo_iterator = Fibonacci(20)
for i in fibo_iterator:
    print(i)


# 0 1 1 2 3 5 8 13 ..




