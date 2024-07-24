
# a='WelComE'
# import re
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
# print(re.search('[A-W]',a))


# import re
# a="abcd"
# print(re.search('[a-z]',a))
# a="abcd123"
# print(re.search('[a-z][0-9]',a))
# print(re.search('[a-z][0-9][0-9]',a))
# a="Aabcd123"
# print(re.search('[A-Z][a-z][0-9][0-9]',a))
# a="AabcCd123"
# print(re.search('[A-Z][a-z][0-9]',a))
# a="Aabcd123"
# print(re.search('[A-Z].*[a-z][0-9]',a))


# print(re.search('[A-Za-z0-9',a))
# print(re.search('[0-9]$',a))
# print(re.search('3$',a))
# print(re.search('6$',a))
# b="welcome"
# print(re.search('e$',b))
# print(re.search('6$',b))
# print(re.search('d$',b))
# print(re.search("welcome$",b))



# number validation
# import re
# a=input("Enter a number")
# if len(a) == 10 and a.isdigit() and re.search('[6-9].{9}',a):
#     print("valid")
# else:
#     print("Invalid")



# email validation
# import re
# a=input("Enter a email ")
# if re.search('[a-z].*[@gmail.com].',a):
#     print("valid")
# else:
#     print("Invalid")


# password validation
# import re
# a=input("Enter a password ")
# pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]).{8,}$"
# if re.search('pattern].',a):
#     print("valid")
# else:
#     print("Invalid")