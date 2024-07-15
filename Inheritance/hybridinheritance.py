
class a:
    def a1(self):
        print('a')
class b:
    def b1(self):
        print('b1')
class f:
    def f1(self):
        print('f1')
class c(a,b):
    def c1(self):
        print("c1")
class d(b,f):
    def d1(self):
        print("d1")
class e(c,d):
    def e1(self):
        print("e1")


e_obj=e()
e_obj.b1()

d_obj=d()
d_obj.b1()

b_obj=b()
b_obj.b1()