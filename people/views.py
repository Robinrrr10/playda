from django.shortcuts import render

# Create your views here.
def allpeople(request):
    return render(request, 'people.html')
