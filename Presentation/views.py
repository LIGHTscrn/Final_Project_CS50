from django.shortcuts import render

app_name = 'presentation'

def home(request):
    return render(request, 'Presentation/home.html')

def demo(request):
    return render(request, 'Presentation/demo.html')

def about(request):
    return render(request, 'Presentation/about.html')

def contact(request):
    return render(request, 'Presentation/contact.html')
