from django.http import HttpResponse

def home(res):
    return HttpResponse('<h1>This is Home page.</h1>')
def contact(res):
    return HttpResponse('<h1>This is Contact page</h1>')

def about(res):
    return HttpResponse('<h1>This is About page.</h1>')