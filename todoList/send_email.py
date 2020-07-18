from django.core.mail import EmailMultiAlternatives
class send_link:
    '''
    the password reset link is generated here and a token is also embedded in it 
    to authenticate the user
    '''
    def send_reset_link(self,token,email):
        url='http://127.0.0.1:4200/password-reset/'+email+'/'+str(token)
        subject, from_email, to = 'testing email', 'bryanreddy23@gmail.com', email
        text_content = 'This is an important message.'
        html_content = '<p>this is the link to reset password <a href='+url+'>click here</a> </p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()