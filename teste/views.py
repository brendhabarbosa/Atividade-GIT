from django.shortcuts import render

# Create your views here.
def brendha(request):
    return render(request, 'brendha.html')
def raquel(request):
    return render(request, 'raquel.html')
def index(request):
    return render(request, 'index.html')