from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.shortcuts import render
from json2html import *
import requests
import json

prefix = """
PREFIX recipe: <http://www.semanticweb.org/andrea/ontologies/2015/10/recipes#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

def q1():

    query1 = """
    SELECT ?recipe_name ?predicate ?object
    WHERE {
    ?subject recipe:Recipe_Name ?recipe_name.
    ?subject recipe:Preparation_Time ?object.
      {?subject recipe:Has recipe:Corn_Flour}
     UNION
    {?subject recipe:Has recipe:Flour}
    } ORDER BY ?object
    """
    payload1 = {'query': prefix + query1}
    r1 = requests.get("http://localhost:3030/ds/query", params=payload1)
    return json2html.convert(json = r1.json(), table_attributes="class=\"table table-bordered table-hover\"")

def q2():

    query2 = """
    SELECT ?recipe_name ?object ?ingredient_name
    WHERE {
      	?subject ?predicate recipe:Christmas.
        ?subject recipe:Recipe_Name ?recipe_name.
        ?subject recipe:Has_Nationality recipe:Venezuelan.
        ?subject recipe:Has ?object.
        ?object recipe:Ingredient_Name ?ingredient_name
    }
    """
    payload2 = {'query': prefix + query2}
    r2 = requests.get("http://localhost:3030/ds/query", params=payload2)
    return json2html.convert(json = r2.json(), table_attributes="class=\"table table-bordered table-hover\"")

def q3():

    query3 = """
    SELECT ?recipe_name (COUNT(?ingredient_name) as ?ingredient_count)
    WHERE {
         ?subject recipe:Recipe_Name ?recipe_name.
         ?subject recipe:Has ?object.
         ?object recipe:Ingredient_Name ?ingredient_name
    }
    GROUP BY ?recipe_name
    HAVING (?ingredient_count < 4)
    """
    payload3 = {'query': prefix + query3}
    r3 = requests.get("http://localhost:3030/ds/query", params=payload3)
    return json2html.convert(json = r3.json(), table_attributes="class=\"table table-bordered table-hover\"")

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
