from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .helpers import GetBody
# Create your views here.

class FirstView(View):
    def get(self, request):
        return JsonResponse({"hello": "world-get"})
    
    def post(self, request):
        return JsonResponse({"hello": "world-post"})
    
    def put(self, request):
        return JsonResponse({"hello": "world-put"})
    
    def delete(self, request):
        return JsonResponse({"hello": "world-delete"})
    
def functionview(request):
    return JsonResponse({"hey":"it works"})

def templateview(request):
    return render(request,"cheese.html", {"hello": "hello world"})

class SecondView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse(
            {"param": param, "query": query, "bread": bread}
            )
        
    def post(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse(
            {"param": param, "query": query, "bread": bread}
            )
        
    def put(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse(
            {"param": param, "query": query, "bread": bread}
            )
        
    def delete(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse(
            {"param": param, "query": query, "bread": bread}
            )
        
class ThirdView(View):
        def post(self, request):
         return JsonResponse(GetBody(request))