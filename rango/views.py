from django.shortcuts import render
from rango.models import Page
from django.http import HttpResponse
from rango.models import Category

def index(request):
    #construct a dictionary to pass to the template engine as its context
    #note the key boldmessage matches to {{ boldmessage }} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['page'] = pages_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    
    return HttpResponse("It works!")

def about(request):
    about_context_dict = {'boldmessage': 'Rango says here is the about page'}
    return render(request, 'rango/about.html', about_context_dict)

def show_category(request, category_name_slug, ):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Category.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request, 'rango/category.html', context=context_dict)