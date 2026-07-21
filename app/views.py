from django.shortcuts import render
from app.models import Registration
from app.forms import RegistrationForm
# Create your views here.
def home(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')
def signup(req):
    form=RegistrationForm()
    if req.method=="POST":      
        form=RegistrationForm(req.POST)
    
        if form.is_valid():
            stu_name=form.cleaned_data["stu_name"]
            stu_email=form.cleaned_data["stu_email"]
            stu_city=form.cleaned_data["stu_city"]
            stu_mobile=form.cleaned_data["stu_mobile"]
            stu_password=form.cleaned_data["stu_password"]
            stu_confirm_password=form.cleaned_data["stu_confirm_password"]

            print(stu_name,stu_email,stu_city,stu_mobile)
            
            if stu_password != stu_confirm_password:
                msg = "Password Not Matching"
                return render(req,"singup.html",{"form":form,"msg":msg})

            user = StudentModel.objects.filter(stu_email=stu_email)
            
            if user:
                msg = "Email already exit"
                form = RegistrationForm()
                return render(req,"signup.html",{"form":form,"msg":msg})
            else:
                form.save()
                msg="Registration succesfull"
                form=RegistrationForm()
                return render(req,"signup.html",{"form":form,"msg":msg})
            
    else:
        return render(req,'signup.html',{"form":form})
def login(req):
    return render(req,'login.html')