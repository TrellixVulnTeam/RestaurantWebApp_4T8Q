from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import sessions

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



#main home view - templateView used in that purpose,

class MainView(TemplateView):
    template_name = 'BasicBusinessManager/WebHtmls/EN/Main.html'
    
    # sends context data to html. It has to be "get_context_data"
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'chuj': self.kwargs.get('chuj', "sda"),
            #'var2': self.kwargs.get('var2', None),
        })
        return context

class ContactView(TemplateView):
    template_name = 'BasicBusinessManager/WebHtmls/EN/Contact.html'

def logout_view(request):
    print("logout")
    logout(request)
    #return redirect('BasicBusinessManager:main')
    return HttpResponseRedirect(reverse('BasicBusinessManager:main'))

def login_view(request):
    chuj = "chuj"
    if request.method == "POST":
        if request.POST.get('submit') == 'login':
            # your sign in logic goes here
            
            print(request.POST.get('login'))

            '''form = MyForm(request.POST)

            print(form['login'].value())
            print(form.data['login'])

            if form.is_valid():

                print(form.cleaned_data['login'])
                print(form.instance.login)

                #form.save()
            print(form.instance.id) # now this one can access id/pk'''
            
            #finds data in html looking for name in html
            login_data = request.POST.dict()
            username = login_data.get("login")
            password = login_data.get("pwd")
            remember_me = login_data.get("remember-me-checkbox")
            print(username, password, remember_me)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if request.user.is_authenticated:
                    #request.sessions['user']=user
                    print("user zalog")
                    return HttpResponseRedirect(reverse('BasicBusinessManager:main'))
            else:
                print("user to zjeb")

            chuj = password

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            
            #return HttpResponseRedirect(reverse('BasicBusinessManager:login_result'))
            return HttpResponseRedirect(reverse('BasicBusinessManager:main'))
            #return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html', {'chuj': chuj})
            #login = question.choice_set.get(pk=request.POST['login'])
        elif request.POST.get('submit') == 'sign_up':
            # your sign up logic goes here
            chuj = "pytong"
            return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html', {'chuj': chuj})
    
    return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html', {'chuj': "brak post"})

class AccountVerifying:
    def authenticate(self, request, username=None, password=None):
        # Check the username/password and return a user.
        ...