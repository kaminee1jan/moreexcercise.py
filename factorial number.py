def fectorial(a):
    fac=1
    while a>0:
        fac=fac*a
        a=a-1
    print("fectorialnumber",fac)
a=int(input("enter the number"))
fectorial(a)