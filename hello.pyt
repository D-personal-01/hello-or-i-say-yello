import random
a="H"
b="E"
c="L"
d="L"
e="O"
a1=0
a2=0
a3=0
a4=0
a5=0
def rand():
    for i in range(0,1000):
        no=random.randint(10000,20000)
        ram=0
        rem=0
    for i in range (0,5):
        rem=no%10
        ram=no//10
        if rem==1:
            print(a,end="")
        elif rem==2:
            print(a.lower(),)