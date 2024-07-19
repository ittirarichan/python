# from abc import ABC,abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         print("sound")
# class bird(animal):
#     def fly(self):
#         print('fly')
#     def make_sound(self):
#         print('bird sound')
# class cat(animal):
#     def run(self):
#         print("run")
#     def make_sound(self):
#         print("cat sound")


# b1=bird()
# b1.fly()
# b1.make_sound()
# print('cat')
# c=cat()
# c.run()


a='WelComE'
import re
# print(re.sub('w','W',a))
# print(re.sub('welcome','PYTHON',a))
# print(re.split('e',a))
# print(re.split('e',a,1))
# print(len(re.findall('e',a)))
# print(re.search('z',a))

# if re.search('w',a):
#     print("yes")
# else:
#     print("No")

# print(re.search('welcome',a))
# print(re.search('d.',a))
# print(re.search(a,a))
# print(re.search('d',a))
# print(re.search('a.',a))
# print(re.search('b.',a))
# print(re.search('c.',a))
# print(re.search('d.',a))
# print(re.search('b..',a))
# print(re.search('a.*',a))
# print(re.search('d.*',a))
# print(re.search('a.+',a))
# print(re.search('d.+',a))
# print(re.search('c.+',a))
# print(re.search('c.?',a))
# print(re.search('d.?',a))
# print(re.search('a.?',a))
print(re.search('[A-W]',a))
