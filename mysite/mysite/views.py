from django.template.loader import get_template
from django.shortcuts import render
from queries import q1, q2, q3

def home(request):
    title = "<h1>Recipe Ontology</h1>"
    return render(request, 'template.html', {'query_content': title})

def query1(request):
    return render(request, 'template.html', {'query_content': q1()})

def query2(request):
    return render(request, 'template.html', {'query_content': q2()})

def query3(request):
    return render(request, 'template.html', {'query_content': q3()})

def queries(request):
    queries = q1() + "<br><br>" + q2() + "<br><br>" + q3()
    return render(request, 'template.html', {'query_content': queries})
