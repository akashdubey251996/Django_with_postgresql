from django.shortcuts import render,redirect
from application1.models import MyModel
from application1.forms import MyForm

# Create your views here.
def add(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name=request.POST['name']
            ins=MyModel(name=name)
            ins.save()

    return render(request,'application1/add.html',{'form',form})
    
  
def suc(request):
    return render(request,'application1/c.html')



