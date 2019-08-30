from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .utils import is_pc

# Create your views here.

def contact(request):
    if is_pc(request.META['HTTP_USER_AGENT']):
        return render(request, 'contact_us.html')
    else:
        return render(request, 'contact_us_mobile.html')


def contact_address(request, link):
    print("Contact_address entered")
    if (link == 'weibo'):
        return HttpResponse('<h1>Weibo Account</h1>')
    elif(link == 'wechat'):
        return HttpResponse('<h1>Wechat Account</h1>')
    elif(link == 'phone'):
        return HttpResponse('<h1>Phone Number</h1>')
    else:
        return HttpResponseNotFound("This address does not exist.")
