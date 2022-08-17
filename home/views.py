from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    s = """
    <h1 style='color: green'>Hello World!</h1>
    <p>lorem ipsum</p>
    <hr/>

    """
    return HttpResponse(s)

def test(request):
    return HttpResponse("test url")