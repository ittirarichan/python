class synnefo:
    def __init__(s):
        print("register")
    def python(s):
        print("Python in synnefo")
    def php(self):
        print('php',self)

class novavi:
    def dm(self):
        print("dm")
    def web_dev(self):
        print("web_dev")
class std(novavi,synnefo):
    def reg(self):
        print("std reg")


manu=synnefo()
manu.python()

sanu=novavi()
sanu.web_dev()

anu=std()
anu.reg()