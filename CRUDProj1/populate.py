import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUDProj1.settings')

import django
django.setup()
from crudApp.models import Student

from faker import Faker
from random import *
fakergen=Faker()
#print(fakergen.phone_number())
def phonenumbergen():
    digit_1=randint(6,9)
    num=str(digit_1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

#print(phonenumbergen())

def student_info_gen(n):
    for i in range(n):
        frollno=fakergen.random_int(min=1,max=999)
        fname=fakergen.name()
        fdob=fakergen.date()
        fmarks=fakergen.random_int(min=1,max=100)
        femail=fakergen.email()
        fphonenumber=phonenumbergen()
        faddress=fakergen.address()
        student_record=Student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,
                                                     email=femail,phonenumber=fphonenumber,address=faddress)
n=int(input('Enter How Many Records Want to Enter'))
student_info_gen(n)