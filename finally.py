# def divide(a,b):
#     try:
#         print (a / b)
#     finally:
#         print ("1234567890-")
# divide(4,1)

# def g():
#     while True:
#         try:
#             reply = int (input('Enter a number \n'))
#             print ("мы ввели число и зашли сюда")
#             #return reply
#         except:
#             print ('Not a number! Try again')
#         continue
# g()


# def rUmnI(r, i):
#     if r <=0 or i<=0:
#         raise ValueError("одно из значений меньше нуля")
#     p=r*i
#     return p
# y=rUmnI(1,0)
# print (y)
#
#
#
# class InvalidTriangleError(Exception):
#     """Raised when a triangle has invalid sides"""


# def rUmnI(r, i):
#     if r <=0 or i<=0:
#         raise InvalidTriangleError("одно из значений меньше нуля")
#     p=r*i
#     return p
# y=rUmnI(1,0)
# print (y)


# def rUmnI(r, i):
#     if r <=0 or i<=0:
#         raise InvalidTriangleError ("одно из значений меньше нуля")
#     p=r*i
#     return p
# y=rUmnI(1,3)
# print (y)
#
#
# try:
#     sq=rUmnI(5,0)
# except  InvalidTriangleError as ex:
#     print(ex)
# else:
#     print(sq)

# import unittest
# import fizz_buzz
#
# class FizzBuzzTests (unittest.TestCase)
#
# def test_fizz(self):
#
# def get_reply(number):
#     if number % 5 == 0 and number & 3 ==0:
#         return "FizzBuzz"
#         elif number % 3 == 0:
#         return "Fizz"
#         elif number % 5 == 0:
#         return "Buzz"
#         else:
#         return " "


# class Character():
#     pass
#
# unit = Character()
# print (type(unit))


# class Character():
#     def __init__(self, race, damage, armor):
#         self.race=race
#         self.damage=damage
#         self.armor=armor
#
# unit = Character("Elf", damage=10, armor=20)
# print(type (unit))
# print (unit.race)
# print (unit.damage)
# print (unit.armor)
#
#
#
# class Character():
#
#     max_speed = 100
#     dead_health = 0
#
#     def __init__(self, race, damage, armor):
#         self.race=race
#         self.damage=damage
#         self.armor=armor
#         self.health = 100
#     def hit (self, damage):
#         self.health -= damage
#     def is_dead(self):
#         return self.health == Character.dead_health
#
# unit = Character("Elf", damage=10, armor=20)
#
#
# # unit.health=100
# # # print (unit.is_dead())
# # print (Character.max_speed)
# Character.max_speed=10
# print (Character.max_speed)


# class Character():
# # #     MAX_SPEED = 100
# # #     def __init__(self, race, damage=10):
# # #         self.damage=damage
# # #         self._race=race
# # #
# # # # Character.MAX_SPEED = 10
# # # # print (Character.MAX_SPEED)
# # # c=Character("Elf")
# # # print (c)
# # # c._race = 'Ork'
# # # print (c._race)


# class Character():
#      MAX_SPEED = 100
#      def __init__(self, race, g=10):
#          self.g=g
#          # self.__race=race
#          # self._health = 100
#          # self._current_speed = 20
#
#      # def hit (self, g):
#      #     self._health -= g
#      @property
#      def health (self):
#         return self._health
#      @property
#      def race (self):
#         return self.__race
#      # @property
#      # def damage (self):
#      #    return self.__damage
#
# c = Character('Elf')
#
# # c._health = 0
# # print (c._health)
#
# c._health = 10
# print (c._health)
#
# c.__race = 40
# print (c.__race)


# class Character():
#     x = 1
#
# t1 = Character()
#
#
# print (Character.x)
# print (t1.x)
#
# t1.x=2
#
# print (Character.x)
# print (t1.x)
#
# Character.x = 3
#
# print (Character.x)
# print (t1.x)


# class Person:
#     name = "Ivan"
#     age = 30
#
#
# a = Person()
# print (Person())
# print(a)
#
# print (Person.__dict__)
# print (a.__dict__)
#
# # Person.age = 10
#
# Person()
# print (a)


# class Car:
#     model = "BMW"
#     engine = 1.6
#
# a = Car()
#
# print (a.__dict__)
# print (a.model)
# print (a.engine)
#
# from enum import Enum
#
#
# class TrafficLight(Enum):
#     RED = 1
#     YELOW = 2
#     GREEN = 3
#
#
# print(TrafficLight(1))
#
#
# class TrafficLight(Enum):
#     RED = 1
#     YELOW = 2
#     GREEN = 3
#
#
# print(TrafficLight(1))


# class Cat:
# #
# #     def __init__(self):
# #         # self.name=name
# #         # self.age=age
# #         # self.poroda = poroda
# #         print ("fff")
# #
# #
# #
# # a = Cat ()


def title (self):
    title = "ABC"
    print (self.title)