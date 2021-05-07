def maximum(a,b,c):
    if a>b and a>c:
        print(a,"a maximum")
    elif b>a and b>c:
        print(b,"b maximum")
    elif c>a and c>b:
        print(c,"c maximum")
    else:
        print("equle")
a=int(input("enter the numbe"))
b=int(input("enter the number"))
c=int(input("enter the number"))
maximum(a,b,c)