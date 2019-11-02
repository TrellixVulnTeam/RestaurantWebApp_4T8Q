from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import sessions
from django.contrib.auth.models import User
from .models.users.employee import Employee
from .models.users.company_owner import CompanyOwner
from .models.users.client import Client

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



#main home view - templateView used in that purpose,

class MainView(TemplateView):
    template_name = 'BasicBusinessManager/WebHtmls/EN/Home.html'
    
    # sends context data to html. It has to be "get_context_data"
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'var1': self.kwargs.get('var1', "sda"),
            #'var2': self.kwargs.get('var2', None),
        })
        return context
def settings_view(request):
    if request.user.is_authenticated:
        return render(request, 'BasicBusinessManager/WebHtmls/EN/Settings.html')
    else:
        return HttpResponseRedirect(reverse('BasicBusinessManager:main'))

def settings_submit_view(request):
    print("submit settings")
    settings_data = request.GET.dict()
    #firstname = request.POST.get('firstname')
    firstname = settings_data.get('firstname')
    print(firstname)
    return HttpResponseRedirect(reverse('BasicBusinessManager:settings'))

class ContactView(TemplateView):
    template_name = 'BasicBusinessManager/WebHtmls/EN/Contact.html'

def logout_view(request):
    print("logout")
    logout(request)
    #return redirect('BasicBusinessManager:main')
    return HttpResponseRedirect(reverse('BasicBusinessManager:main'))

def login_view(request):
    if request.method == "POST":
        # backend finds object (get) using html - name then check its value
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
                    print("user logged in")
                    return HttpResponseRedirect(reverse('BasicBusinessManager:main'))
            else:
                print("wrong user data")

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            
            #return HttpResponseRedirect(reverse('BasicBusinessManager:login_result'))
            return HttpResponseRedirect(reverse('BasicBusinessManager:main'))
            #return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html', {'chuj': chuj})
        elif request.POST.get('submit') == 'sign_up':
            # takes data from inputs by name
            sign_up_data = request.POST.dict()
            email = sign_up_data.get("sign-up-email")
            username = sign_up_data.get("sign-up-username")
            password = sign_up_data.get("sign-up-pwd")
            confirmation_password = sign_up_data.get("sign-up-confirm-pwd")
            account_type = sign_up_data.get("type-sel")

            #checks if data is filled
            error_msg = ""
            if email == "" or email is None:
                error_msg += " Empty data fields "
            if username == "" or username is None:
                error_msg +=" Empty data fields "
            if error_msg != "":
                return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html',{'wrong_pwd':error_msg})   

            # checks account type then creates user and his child object. Before chcecks if both passwords are the same
            if (password == confirmation_password) and (password != "" and confirmation_password != ""):
                if account_type=="Client":
                    user = User.objects.create_user(username,email,password)
                    client = Client.objects.create_client(user)
                    user.save()
                    client.save()
                elif account_type=="Employee":
                    user = User.objects.create_user(username,email,password)
                    employee = Employee.objects.create_employee(user)
                    user.save()
                    employee.save()
                elif account_type=="Business client":
                    user = User.objects.create_user(username,email,password)
                    owner = CompanyOwner.objects.create_owner(user)
                    user.save()
                    owner.save()
                return HttpResponseRedirect(reverse('BasicBusinessManager:main'))
            else: 
                #if passwords are incorrect it renderds en/login/ page showing modal with "wrong password" info
                return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html',{'wrong_pwd':"Password and Confirmation password are not the same or empty !"})
    
    return render(request, 'BasicBusinessManager/WebHtmls/EN/Main.html')

class AccountVerifying:
    def authenticate(self, request, username=None, password=None):
        # Check the username/password and return a user.
        ...