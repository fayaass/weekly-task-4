from user import *
from login import *
from list import *





def add_fwr():
    if len(fwr)==0:
        id=201
    else:
        id=fwr[-1]['id']+1
    f1=0
    for i in fwr:
        if i['id']==id:
            f1=1
            add_fwr()
    if f1==0:
        name=str(input('enter the name :'))
        price=int(input('enter the price :'))
        stock=int(input('enter the stock'))
        fwr.append({'name':name,'id':id,'price':price,'stock':stock})


def view_fwr():
    for i in fwr:
        print(i)


def update_fwr():
    id=int(input('enter id :'))                                                         
    f1=0
    for i in fwr:
        if i['id']==id:
            f1=1
            price=int(input('enter price :'))                                   
            stock=str(input('enter stock :'))
            i['price']=price
            i['stock']=stock
    if f1==0:
        print('invalid id')



def delete():
    id=int(input('enter id :'))
    f1=0
    for i in fwr:
        if i['id']==id:
            f1=1
            fwr.remove(i)

    if f1==0:
        print('invalid id')