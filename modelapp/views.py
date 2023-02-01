from django.shortcuts import render, redirect
from modelapp.forms import UserForm
from modelapp.models import UserModel

# Create your views here.
def createview(request):
    fm = UserForm(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            reg = UserModel(name=nm,email=em)
            reg.save()
            return redirect('home')
    else:
        fm = UserForm()
    out = UserModel.objects.all()
    return render(request,'home.html',{'form':fm,'data':out})

def successpage(request):
    return render(request,'success.html')