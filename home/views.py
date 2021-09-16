from django.shortcuts import render

# Create your views here.
def home(request):
    result={}
    return render(request, 'home.html', context=result)

def premium(request):
    result={}
    return render(request, 'premium.html', context=result)

def frame_test(request):
    result={}
    return render(request, 'frame_test.html', context=result)