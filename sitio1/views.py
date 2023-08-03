from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1>Welcome to home page</h1>")