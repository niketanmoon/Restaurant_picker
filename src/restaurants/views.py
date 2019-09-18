from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#function based view
def home(request):
    html_var = 'f string'
    html_ = f"""<!DOCTYPE html>
        <html lang=en>
        <head>
        </head>
        <body>
            <h1>Hello World</h1>
            <p>This is {html_var} coming through</p>
        </body>
        </html>
    """
    return HttpResponse(html_)
