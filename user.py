
from admin import *
from login import *
from list import *













def view_profile(log):
    print(log)


def update_profile(log):

    name=str(input('enter name :'))
    phone=int(input('enter phone :'))
    log['name']=name
    log['phone']=phone
  


def buy_fwr(log):
    id=int(input('enter id :'))
    f=0
    for i in fwr:
        if i['id']==id:
            f=1
            i['stock']-=1
            log['fwrs'].append(id)
            print('shoes added')
    if f==0:
        print('invalid id')




def fwr_in_hand(log):
    print(log['fwrs'])