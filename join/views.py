from django.shortcuts import render , HttpResponseRedirect
from .forms import UserRegistrationForm
from  .models import User

# Create your views here.

# Show  data  and   add data  
def join(request):
    if request.method == 'POST':
        fm = UserRegistrationForm(request.POST)
        if fm.is_valid():
            name =fm.cleaned_data['name']
            email =fm.cleaned_data['email']
            password =fm.cleaned_data['password']
            user=User(name=name,email=email,password=password)
            user.save()
            fm = UserRegistrationForm()
    else:
        fm = UserRegistrationForm()
    alluser=User.objects.all()
    return render(request, 'join/base.html', {'form': fm,'alluser':alluser})

# Delete function 
def delete(request,id):
    if request.method == 'POST':
        item = User.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect('/')