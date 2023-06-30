from django.shortcuts import render

def index(request):
    context = {}
    return render(request=request, template_name='pages/index.html', context=context)