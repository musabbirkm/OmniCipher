from django.http import JsonResponse
from django.shortcuts import render
from home.models import Contact

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")

        ins = Contact(name=name,email=email,number=number,message=message)
        ins.save()
        response_data = {
            "status": "success",
            "message": "Contact form submitted successfully!",
        }
        return JsonResponse(response_data)

    return render(request, "contact.html")

def projects(request):
    return render(request,"project.html")

def services(request):
    return render(request,"services.html")

def blogs(request):
    return render(request,"blogs.html")

def blog1(request):
    return render(request,"blog1.html")

def blog2(request):
    return render(request,"blog2.html")

def blog3(request):
    return render(request,"blog3.html")

def blog4(request):
    return render(request,"blog4.html")

def blog5(request):
    return render(request,"blog5.html")

def blog6(request):
    return render(request,"blog6.html")

def blog7(request):
    return render(request,"blog7.html")

def blog8(request):
    return render(request,"blog8.html")