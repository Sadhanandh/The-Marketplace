# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Publicdb
import json

register = template.Library()

class Data:
    def __init__(self):
        self.name = "Apple Mac"
        self.desc = "This is a discription of the data ..."
        self.mrp = "50"
        self.crp = "50"
        self.image = "/static/js/holder.js/300x200"

    def Name(self):
        return self.name
    def Desc(self):
        return self.desc
    def Mrp(self):
        return self.mrp
    def Crp(self):
        return self.crp
    def Url(self):
        return self.image


    
@login_required()
def interface_view(request):
    data = None
    data = [Data()]*3
    data = Publicdb.objects.all()
    search = request.POST.get("search",None)
    pageno = request.POST.get("page",None)
    pageval = 1000
    if search !=None:
#        data="" #getdata
        data = [Data()]*3
    return render_to_response('queries.html',{"data":data,"page":pageno,"pageval":pageval,"username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))

@login_required()
def jinterface(request):
    data = Publicdb.objects.all()
    pageno = 0
    pageval = 1000
    return render_to_response('queries.html',{"base_template":"customajax.html","data":data,"page":pageno,"pageval":pageval,"username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))

@login_required()
def typehead(request):
    qry = request.GET.get("query")
    json_data='{ "options":[]}'
    if qry!=None:
        json_data = json.dumps({"options":["new","man","can"]})
    return HttpResponse(json_data,content_type="application/json")

@login_required()
def jgetquery(request):
    data = None
    data = [Data()]*2
    search = request.GET.get("search",None)
    pageno = request.GET.get("page",None)
    pageval = 1000
    if search !=None:
        data="" #getdata
        if search==1:
            data = [Data()]*1
        else:
            data = [Data()]*int(search)
            
    return render_to_response('queries.html',{"data":data,"page":pageno,"pageval":pageval,"inner_template":"ajax.html","username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))
        