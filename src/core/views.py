# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from django.http import HttpResponse
import json

def index(request):
    template_name = "index.html"
    context = {}
    licencias = Licencia.objects.all()
    print licencias
    context["licencias"] = licencias
    print context
    return render(request,template_name,context)

def crear_licencia(request):
    print request.POST
    licencia = Licencia.objects.create(name=request.POST["name"],
                                      description=request.POST["description"])
    licencia.save()
    html = '<tr><td>'+str(licencia.pk)+'</td><td>'+str(licencia.name)+'</td><td>'+str(licencia.description)+'</td></tr>'
    response = {"ok":"ok","html":html}
    return HttpResponse(json.dumps(response),content_type="application/json")