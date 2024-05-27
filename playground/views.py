from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 3
    y = 4
    return x+y

def say_hello(request):
    sum = calculate()
    return render(request, 'hello.html', {'name': 'Kamrul', 'sum': sum})
