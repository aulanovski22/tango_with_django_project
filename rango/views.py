from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its context
    #note the key boldmessage matches to {{ boldmessage }} in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    
    return HttpResponse("It works!")

def about(request):
    context_dict = {'boldmessage': 'The cat was here!'}
    return render(request, 'rango/about.html', context=context_dict)
