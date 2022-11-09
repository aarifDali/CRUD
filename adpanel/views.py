from django.shortcuts import render,redirect
from django.contrib import messages
from authentication.views import home
from adpanel.models import UserProfile
from adpanel.forms import UserRegistration
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Create your views here
 




@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def userdisplay(request):

    usr = User.objects.all()
    return render(request, 'admin/userdisplay.html', {'usr': usr})



@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        messages.info(request, 'Deleted Succefully')
    return redirect('userdisplay')    



@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        
        fm = UserRegistration(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Edited Succefully')
        
    else:
        pi = User.objects.get(pk = id)
        fm = UserRegistration(instance=pi)
        
    return render(request, 'admin/userupdate.html', {'form' : fm})




@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def search_username(request):
    searched = request.GET['search']
    searchnames = User.objects.filter(username__contains = searched)
    return render(request, 'admin/userdisplay.html', {'usr' : searchnames}) 

    