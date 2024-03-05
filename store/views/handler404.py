from django.shortcuts import render

def Handler404(request, exception):
    return render(request, '404.html', status=404)
