from django.shortcuts import render

def homepage(request):
    context = {}
    return render(request, 'mainApp/mainTemplate.html', context)
