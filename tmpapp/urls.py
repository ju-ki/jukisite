from tmpapp import views
from django.urls import path


app_name = "tmpapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("", views.SkillView.as_view(), name="skill")
]
