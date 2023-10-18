from django.shortcuts import render
from .models import Resume
from .forms import resumeform
from django.views import View

#def hi(request):
    #if request.method=='POST':
        #fm=resumeform(request.POST,request.FILES)
        #if fm.is_valid():
            #fm.save()
    
    #else:
        #fm = resumeform()
    #return render(request,'myapp/home.html',{'form':fm})


class hello(View):
    def get(self,request):
        fm = resumeform()
        candidate=Resume.objects.all()
        return render(request,'myapp/home.html',{'candidate':candidate,'form':fm})

    def post(self,request):
        fm=resumeform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = resumeform()
            return render(request,'myapp/home.html',{'form':fm})

class candidateview(View):
    def get(self,request,pk):
        candidate=Resume.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate':candidate})

# Create your views here.
