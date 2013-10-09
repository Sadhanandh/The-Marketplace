# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

@login_required()
def interface_view(request):
    return render_to_response('interface.html',{"username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))

@login_required()
def jinterface(request):
    return render_to_response('interface.html',{"base_template":"ajax.html","username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))