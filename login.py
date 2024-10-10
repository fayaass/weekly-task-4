from user import *
from admin import *
from main import *
from list import *





def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    
    email=str(input('enter email :'))
    f1=0
    for i in user:
            if i['email']==email:
                f1=1
                register()
    if f1==0:
            name=str(input('enter the name :'))
            username=email
            phone=int(input('enter phone no :'))
            password=input('enter the password :')
            user.append({'name':name,'id':id,'email':email,'fwrs':[],'phone':phone,'password':password})


def login():
    uname=input('enter uname')
    passw=input('enter passw')
    f=0
    if uname=='admin' and passw=='admin':
        f=1
    log=''
    for i in user:
        if uname==i['email'] and passw==i['password']:
            f=2
            log=i
    return f,log   