from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):
    return render(request, "core/index.html")

def services (request):
    return render(request, "core/services.html")

def contact (request):
    return render(request, "core/contact.html")

def team (request):
    return render(request, "core/team.html")

def about (request):
    return render(request, "core/about.html")

def portfolio (request):
    return render(request, "core/portfolio.html")