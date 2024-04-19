# Задание 1
# К уже реализованному классу «Дробь» добавьте ста-
# тический метод, который при вызове возвращает коли-
# чество созданных объектов класса «Дробь».
#
# def nod(num1, num2):
#     if num2 % num1 == 0:
#         return num1
#     return nod(num2 % num1, num1)
#
#
# class Fraction:
#     i = 0
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction.i += 1
#
#     def __del__(self):
#         Fraction.i -= 1
#
#     def summarise(self, other):
#         new_num = self.numerator * other.denominator + self.denominator * other.numerator
#         new_denom = self.denominator * other.denominator
#         reduction = nod(new_num, new_denom)
#         return Fraction(new_num // reduction, new_denom // reduction)
#
#     def difference(self, other):
#         new_num = self.numerator * other.denominator - self.denominator * other.numerator
#         new_denom = self.denominator * other.denominator
#         reduction = nod(new_num, new_denom)
#         return Fraction(new_num // reduction, new_denom // reduction)
#
#     def multiplication(self, other):
#         new_num = self.numerator * other.numerator
#         new_denom = self.denominator * other.denominator
#         reduction = nod(new_num, new_denom)
#         return Fraction(new_num // reduction, new_denom // reduction)
#
#     def division(self, other):
#         new_num = self.numerator * other.denominator
#         new_denom = other.numerator * self.denominator
#         reduction = nod(new_num, new_denom)
#         return Fraction(new_num // reduction, new_denom // reduction)
#
#     def __str__(self):
#         if self.denominator == 1:
#             return f'{self.numerator}'
#         return f'{self.numerator}/{self.denominator}'
#     @staticmethod
#     def quantity():
#         return f'{Fraction.i} созданных дробей'
#
#
# fr1 = Fraction(5, 10)
# fr2 = Fraction(1, 4)
# del fr2
#
# print(Fraction.quantity())


# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фа-
# ренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.


# class ConverterDegree:
#     i = 0
#
#     @staticmethod
#     def c_to_f(c):
#         ConverterDegree.i += 1
#         return c * 1.8 + 32
#
#     @staticmethod
#     def f_to_c(f):
#         ConverterDegree.i += 1
#         return (f - 32) / 1.8
#
#     @staticmethod
#     def quantity():
#         return f'Произведено {ConverterDegree.i} подсчетов температуры'
#
# print(ConverterDegree.c_to_f(-40))
# print(ConverterDegree.f_to_c(-40))
# print(ConverterDegree.f_to_c(-40))
# print(Degree.quantity())
# class ConverterValue:
#         @staticmethod
#         def metr_to_inch(metr):
#             return metr * 39.37
#
#         @staticmethod
#         def metr_to_foot(metr):
#             return metr * 3.28
#
#         @staticmethod
#         def metr_to_mile(metr):
#             return metr * 0.000621
#
#         @staticmethod
#         def kg_to_pound(kg):
#             return kg * 2.2
#
#         @staticmethod
#         def liter_to_ounce(liter):
#             return liter * 35.2
#
#         @staticmethod
#         def inch_to_metr(inch):
#             return inch /39.37
#
#         @staticmethod
#         def foot_to_metr(foot):
#             return foot / 3.28
#
#         @staticmethod
#         def mile_to_metr(mile):
#             return mile / 0.000621
#
#         @staticmethod
#         def pound_to_kg(pound):
#             return pound / 2.2
#
#         @staticmethod
#         def ounce_to_liter(ounce):
#             return ounce / 35.2
#
#
# print(ConverterValue.pound_to_kg(77))