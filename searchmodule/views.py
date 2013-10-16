# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import RawPublicdb as Publicdb
import json
#from models import Publicdb

register = template.Library()

class Data:
    def __init__(self):
        self.name = "Parle G"
        self.desc = "This is a discription of the data ..."
        self.mrp = "50"
        self.crp = "50"
        self.image = "/static/js/holder.js/300x200"
        self.id = "3"
        self.qty = "500gm"

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
    def Id(self):
        return self.id
    def Qty(self):
        return self.qty


    
@login_required()
def interface_view(request):
    data = None
    data = [Data()]*3
    data = Publicdb.objects.all()
    search = request.POST.get("search",None)
    pageno = request.POST.get("page",None)
    pageval = 1000
    if search !=None:
        q = Publicdb.objects.filter(Q(Name__icontains=search)|Q(Desc__icontains=search))
        data = q
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
        out = set()
        q = Publicdb.objects.filter(Name__icontains=qry).order_by("Name").values("Name")
        for subq in q:
            out.add(subq["Name"])
        json_data = json.dumps({"options":list(out)})
    return HttpResponse(json_data,content_type="application/json")

@login_required()
def jgetquery(request):
    data = None
    data = [Data()]*2
    search = request.GET.get("search",None)
    pageno = request.GET.get("page",None)
    pageval = 1000
    if search !=None and search[:5] == "dummy" and len(search)>5:
        data = [Data()]*int(search[5:])
    elif search !=None:
        q = Publicdb.objects.filter(Q(Name__icontains=search)|Q(Desc__icontains=search))
        data = q
    
            
    return render_to_response('queries.html',{"data":data,"page":pageno,"pageval":pageval,"inner_template":"ajax.html","username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))

@login_required()
def item(request,i_id):
    try:
        data =  Publicdb.objects.get(Id=i_id)
    except Exception :
        raise Http404()
    return render_to_response('item.html',{"element":data,"username":request.user.username,"login": request.user.is_authenticated() },context_instance=RequestContext(request))