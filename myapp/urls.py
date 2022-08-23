from myapp import views
from django.urls import path


app_name = "myapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("introduction/", views.SelfIntroductionView.as_view(), name="introduction"),
    path("skill/", views.SkillView.as_view(), name="skill"),
    path("works/", views.WorkView.as_view(), name="works"),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("experience/", views.ExperienceView.as_view(), name="experience"),
    path("news/", views.NewsView.as_view(), name="news"),
]
