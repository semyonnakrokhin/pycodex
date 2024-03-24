from django.shortcuts import render


def index(request):
    return render(request, 'info/home.html')


def course(request, pk):
    return render(request, f'info/course{pk}.html')
