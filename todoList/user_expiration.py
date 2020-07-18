from .models import user_password_reset_time
import django.utils.timezone as t
# there is a concept of naive time and aware time that comes into play since  USE_TZ=True, all time formats operations
#  must be done using the django.utils.timezone
import datetime as dt
def UserExperation(data):
    '''
    THIS FUNCTION HERE WILL DECIDE WETHER THE THE USER CAN RESEND A FORGOT PASSWORD LINK.
    THE USUAL WAIT TIME FOR A USER BEFORE HE CAN RESEND A LINK IS 5 MINUTES
    '''
    datas=data
    user=user_password_reset_time.objects.filter(user=datas['email']).values()
    a=0
    for i in user: 
        a=i
    if a==0:# IF IT DOESN'T EXIST IN DB THEN THE USER WILL BE ADDED TO DB
        print(a)
        return 'insert'
    else:
        c=t.now()-a['time']
        if c.seconds/60>=5:
            #if time  since last link sent >5 minutes this will be executed
            user_password_reset_time.objects.filter(user=datas['email']).delete()
            return 'can resend link'
        else:
            return 'cannot resend link'