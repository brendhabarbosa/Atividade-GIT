from django.shortcuts import render

# Create your views here.
def brendha(request):
    return render(request, 'index.html')