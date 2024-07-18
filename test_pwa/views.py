from django.shortcuts import render

# Create your views here.


def test_pwa(request):
    return render(request, 'base.html', {})
