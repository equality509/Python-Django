from django.contrib import admin
from django.urls import path
from pets.views import TurtleView, TurtleViewID

urlpatterns = [
    path("admin/", admin.site.urls),
    path("turtle/", TurtleView.as_view()),
    path("turtle/<int:id>", TurtleViewID.as_view())
]