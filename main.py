# MAGIC METHOD
# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __gt__(self, other):  # >
#         return self.age > other.age
#     def __ge__(self, other):   # >=
#         return self.age >= other.age
#     def __lt__(self, other):  # <
#         return self.age < other.age
#     def __le__(self, other): # <=
#         return self.age <= other.age
#     def __eq__(self, other):  # ==
#         return self.age == other.age
#     def __ne__(self, other):  # !=
#         return self.age != other.age
#     @property # agar wunaqa decorator yozilsa funksiya hic narsa qabul qilmaydi oddiy atribute sifatida iwlaydo
#     def info(self):
#        return f"Name {self.name} age {self.age}"
#
#
#
# u1 = User("Usmon",33)
# u2 = User("Anvar",45)
# print(u1<u2)
# print(u1.info)


# decoratorni rucnoy yaratiw  doim @ bn bowlanadi takrorlaniwni oldini oladi ummumiy javob beradi
# def check(func):
#     def inner_func(*args):
#         try:
#             return func(*args)
#         except Exception as e :
#             return f"xatolik: {e}"
#     return inner_func
# @check
# def hisob(a,b):
#     return  a+b
# print(hisob(10,'4'))
#
# @check
# def hisob(a,b):
#     return a/b
# print(hisob(4,0))



# class User:
#     def __init__(self,name,age,job,hour,salary):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.hour = hour
#         self.salary = salary
#     def day_salary(self):
#         return self.hour * self.salary
#     def week_salary(self):
#         return self.day_salary() * 6
#     def moth_salary(self):
#         return self.week_salary() * 4
#     def year_salary(self):
#         return self.moth_salary() * 12
# user = User("Lola",24,"cooker",6,70000)
# print(user.day_salary())
# print(user.week_salary())
# print(user.moth_salary())
# print(user.year_salary())


# class User:
#     def __init__(self,name,age,job):
#         self.name = name # public
#         self._age = age # protected  print(use._age) qilinsa iwlaydi
#         self.__job = job # private  icida nmadir qilsak iwlaydi pastadagiday lkn tawqaridan caqirib mbomaydi
#     def info(self):
#         return f"Iw {self.__job}"
# user = User("fgfd",89,"pkiooh")
# print(user.info())





























































































