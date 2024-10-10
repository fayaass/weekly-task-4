from user import *
from admin import *
from login import *
from list import *


while True:
    print('''
1.register
2.login
3.exit
    ''')
    choice=int(input('enter the choice'))
    if choice==1:
        register()
    elif choice==2:
        f,log=login()

        if f==1:
            while True:
                print('''
                1.add fwr
                2.view fwr
                3.update fwr
                4.delete
                5.view user
                6.exit
                ''')
                sub_ch=int(input('enter the choice :'))
                if sub_ch==1:
                    add_fwr()
                elif sub_ch==2:
                    view_fwr()
                elif sub_ch==3:
                    update_fwr()
                elif sub_ch==4:
                    delete()
                elif sub_ch==5:
                    view_user()
                elif sub_ch==6:
                    break

        elif f==2:
            while True:
                print('''
                1.view profile
                2.view fwr
                3.update profile
                4.buy fwr
                5.fwr in hand
                6.exit
                ''')
                sub_ch=int(input('enter the choice :'))
                if sub_ch==1:
                    view_profile(log)
                elif sub_ch==2:
                    view_fwr()
                elif sub_ch==3:
                    update_profile(log)
                elif sub_ch==4:
                    buy_fwr(log)
                elif sub_ch==5:
                    fwr_in_hand(log)
                elif sub_ch==6:
                    break


        elif f==0:
            print('invalid uname or passw')
    elif choice==3:
        break
    else:
        print('invalid')