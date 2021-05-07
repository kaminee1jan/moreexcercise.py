def name():
    i=0
    c=[]
    while i<len(list1):
        if list1[i]  not in list2:
            c.append(list1[i])
        else:
            c=list2
        i=i+1
    print(c)
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
name()

        