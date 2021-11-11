from django.shortcuts import render
from django.http import HttpResponse
from emaildjango import settings
from django.core.mail import send_mail
from myapp.forms import *

# Create your views here.
def send(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        to = request.POST['to']
        msg = request.POST['msg']
        subject = request.POST['subject']
        if form.is_valid():
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            if res == 1:
                return HttpResponse('Mail sent successfully')
            else:
                return HttpResponse('Mail could not be sent')
        else:
            form = EmailForm()
        return render(request,'send.html',{'form':form})
