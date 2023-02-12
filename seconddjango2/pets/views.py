from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Turtle
from django.views import View
from .helpers import GetBody
from django.core.serializers import serialize

# Create your views here.

class TurtleView(View):
    ## Route to get all Turtles
    def get(self, request):
        ## get all the Turtles
        all = Turtle.objects.all()
        ## Turn the object into a json string
        serialized = serialize("json", all)
        ## Turn the json string into a dictionary
        finalData = json.loads(serialized)
        ## Send json response, turn safe off to avoid errors
        return JsonResponse(finalData, safe=False)
    
    ## Route to create a turtle
    def post (self, request):
        ## get data from the body
        body = GetBody(request)
        print(body)
        ## create new turtle
        turtle = Turtle.objects.create(name=body["name"], age=body["age"])
        ## turn the new turtle into json string then a dictionary
        finalData = json.loads(serialize("json", [turtle])) #turtle in array to be serializable
        ## Send json response
        return JsonResponse(finalData, safe=False)
    
    
# class for "/turtle/<id>" routes
class TurtleViewID(View):
    ## Function to show 1 Turtle
    def get (self, request, id):
        ## get the turtle
        turtle = Turtle.objects.get(id=id)
        ## serilize then turn into dictionary
        finalData = json.loads(serialize("json", [turtle]))
        ## send json response
        return JsonResponse(finalData, safe=False)

    ## Function for updating turtle
    def put (self, request, id):
        ## get the body
        body = GetBody(request)
        ##update turtle
        ## ** is like JS spread operator
        Turtle.objects.filter(id=id).update(**body)
        ## query for turtle
        turtle = Turtle.objects.get(id=id)
        ## serialize and make dict
        finalData = json.loads(serialize("json", [turtle]))
        ## return json data
        return JsonResponse(finalData, safe=False)

    def delete (self, request, id):
        ## query the turtle
        turtle = Turtle.objects.get(id=id)
        ## delete the turtle
        turtle.delete()
        ## serilize and dict updated turtle
        finalData = json.loads(serialize("json", [turtle]))
        ##send json response
        return JsonResponse(finalData, safe=False)
