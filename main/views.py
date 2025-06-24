from django.shortcuts import render

def landingPage(request):
    return render(request,'pages/index.html')

def blogPage(request):
    return render(request,'pages/blog.html')