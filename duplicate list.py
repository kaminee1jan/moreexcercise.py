def duplicate_list():
    i=0
    list=[]
    while i<len(string_list):
        if string_list[i] not in list:
            list.append(string_list[i])
        i=i+1
    print(list)
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble","Humble"]
duplicate_list()
