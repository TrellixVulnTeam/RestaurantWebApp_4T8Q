from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



#main home view - templateView used in that purpose
class MainView(TemplateView):
    template_name = 'BasicBusinessManager/WebHtmls/EN/Main.html'

