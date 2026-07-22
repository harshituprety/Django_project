from django.shortcuts import render
from app.models import Registration
from app.forms import RegistrationForm,LoginForm
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
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email_address=form.cleaned_data["email_address"]
            password=form.cleaned_data["password"]
            confirm_password=form.cleaned_data["confirm_password"]

            print(first_name,last_name,email_address)
            
            if password != confirm_password:
                msg = "Password Not Matching"
                return render(req,"signup.html",{"form":form,"msg":msg})
            else:
                form.save()                                            
                msg = "Registration successful."
                form = RegistrationForm()
                return render(req,"signup.html",{"form":form,"msg":msg})

            user = StudentModel.objects.filter(email_address=email_address)
            
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

def login(req):
    form=LoginForm()
    if req.method == "POST":
        data = LoginForm(req.POST)
        if data.is_valid():
            email = data.cleaned_data['email_address']
            password = data.cleaned_data['password']
            user = StudentModel.objects.filter(email_address=email)

            if user:
                user = StudentModel.objects.get(email_address=email)
                # print(user.stu_password)
                if user.password == password:
                    firstname = user.first_name
                    lastname = user.last_name
                    email = user.email_address
                    password = user.password

                    data = {
                        'firstname':name,
                        'lastname':lastname,
                        'email':email,
                        'password':password
                    }
                    initial_data = {
                        'first_name' : firstname,
                        'last_name' : lastname,
                        'email_address' : email
                    }
                    form1=QueryForm(initial=initial_data)
                    data1=StudentQuery.objects.filter(email_address = email)
                    return render(req,'dashboard.html',{'data':data,'query':form1,'data1':data1})
                else:
                    msg = "Email & Password not matched"
                    return render(req,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(req,'login.html',{'form':form,'msg':msg})
    else:
        return render(req,'login.html',{'form':form})