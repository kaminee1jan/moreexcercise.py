def student(number_of_student,ek_student_ka_kharcha):
    total_kharcha=number_of_students*ek_student_ka_kharcha
    if total_kharcha<=50000:
        print("hm budget ke andar hai")
    else:
        print(" hm budget ka bahr hai")
number_of_students=int(input("enter the number"))
ek_student_ka_kharcha=int(input("enter the number"))
student(number_of_students,ek_student_ka_kharcha)

