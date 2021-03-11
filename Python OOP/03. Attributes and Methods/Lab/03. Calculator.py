class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = 1
        for each in args:
            res *= each
        return res

    @staticmethod
    def divide(start, *args):
        res = start
        for each in args:
            res /= each
        return res

    @staticmethod
    def subtract(start, *args):
        res = start
        for each in args:
            res -= each
        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

