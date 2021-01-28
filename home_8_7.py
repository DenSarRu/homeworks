# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class MyComplexNumber:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        complex_ = self.__complex + other.__complex
        return MyComplexNumber(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        complex_ = self.__complex * other.__complex
        return MyComplexNumber(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


c1 = MyComplexNumber(2, -3)
c2 = MyComplexNumber(2)

print(c1 + c2, complex(2, -3) + complex(5))
print(c1 * c2, complex(2, -3) * complex(5))
