from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
import csv
def insert_bank(self):
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\django projects\\lav\\Scripts\\project15\\app\\bank.csv','r') as FO:
        iod=csv.reader(FO)
        for i in iod:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
        return HttpResponse('bank data inserted successfully')

    
def insert_branch(self):
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\django projects\\lav\\Scripts\\project15\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]
                bro=branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                bro.save()
        return HttpResponse('branch data inserted successfully')