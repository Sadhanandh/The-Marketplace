# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
#from django.views.decorators.csrf import csrf_protect
#from authmodule import authenticate,login,logout,get_username


guest = "guest@gmail.com"
defvalue = " "


def main_view(request):
    username = request.POST.get('username',defvalue)
    password = request.POST.get('password',defvalue)
    user = authenticate(username=username, password=password)
    if user is not None:
            login(request, user)
            #request.user.username = get_username(user)
    
    username = request.user.username
    logmein = request.user.is_authenticated()
    nextpage = request.GET.get("next")
    if nextpage is None:
        nextpage = request.POST.get("nextpage",None)
    if(nextpage!=None and logmein):
        return HttpResponseRedirect(nextpage)
    return render_to_response('homepage.html',{"username":username,"login":logmein,"nextpage":nextpage},context_instance=RequestContext(request))


def login_view(request):
    username = request.POST.get('username',defvalue)
    password = request.POST.get('password',defvalue)
    user = authenticate(username=username, password=password)
    if user is not None:
            login(request, user)
            #request.user.username = get_username(user)
    
    username = request.user.username
    logmein = request.user.is_authenticated()
    nextpage = request.GET.get("next")
    if nextpage is None:
        nextpage = request.POST.get("nextpage",None)
    if(nextpage!=None and logmein):
        return HttpResponseRedirect(nextpage)
    if(nextpage==None and logmein):
        return HttpResponseRedirect('/interface')
    return render_to_response('loginpage.html',{"username":username,"login":logmein,"nextpage":nextpage},context_instance=RequestContext(request))

def jlogin(request):
    uname = request.POST.get('username',defvalue)
    pword = request.POST.get('password',defvalue)
    user = authenticate(username=uname, password=pword)
    if user is not None:
        login(request, user)
        #request.user.username = get_username(user)
         
    username = request.user.username
    logmein = request.user.is_authenticated()
    return render_to_response('logincontent.html',{"base_template":"ajax.html","username":username,"login":logmein},context_instance=RequestContext(request))
             
def logout_view(request):
    logout(request)
    logmein = request.user.is_authenticated()
    return render_to_response('homepage.html',{"username":guest,"login":logmein},context_instance=RequestContext(request))

def jlogout(request):
    logout(request)
    logmein = request.user.is_authenticated()
    return render_to_response('logincontent.html',{"base_template":"ajax.html" ,"username":guest,"login":logmein},context_instance=RequestContext(request))

def register(request):
    us = request.POST.get("username",None)
    pa = request.POST.get("password",None)
    pa1 = request.POST.get("repassword",None)
    if us!=None and pa!=None and pa!=None and pa==pa1:
        try:
            u  = User.objects.create_user(us,us,pa)
            u.save()
            return redirect("mainmodule.views.login_view")
        except Exception:
            return HttpResponseNotAllowed("User name exists.Try again!")
        
    else:
        return HttpResponseNotAllowed("Enter username and password")