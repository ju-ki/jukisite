from django.shortcuts import render
from django.views.generic import View
from .models import ImageModel, SkillModel, IntroductionModel, SelfIntroductionModel, BlogModel, ExperienceModel, ContactModel, NewsModel


class IndexView(View):
    """top page view"""

    def get(self, request, *args, **kwargs):
        introduction = IntroductionModel.objects.all()
        return render(request, "myapp/main.html", {"introduction_data":introduction})


class SelfIntroductionView(View):
    """top page view"""
    def get(self, request, *args, **kwargs):
        about_data = SelfIntroductionModel.objects.all()
        return render(request, "myapp/self_introduction.html", {"about_data":about_data})


class SkillView(View):
    """top page view"""
    def get(self, request, *args, **kwargs):
        skill_data = SkillModel.objects.all()
        return render(request, "myapp/skill.html", {"skill_data":skill_data})


class ContactView(View):
    """top page view"""
    def get(self, request, *args, **kwargs):
        contact_data = ContactModel.objects.all()
        return render(request, "myapp/contact.html", {"contact_data":contact_data})


class BlogView(View):
    """top page view"""
    def get(self, request, *args, **kwargs):
        blog_data = BlogModel.objects.all()
        return render(request, "myapp/blog.html", {"blog_data":blog_data})


class WorkView(View):
    """top page view"""
    def get(self, request, *args, **kwargs):
        skill_data = SkillModel.objects.all()
        return render(request, "myapp/works.html", {"skill_data":skill_data})


class ExperienceView(View):
    """top page view"""
    def get(self, request, *args, **kwargs):
        experience_data = ExperienceModel.objects.all()
        return render(request, "myapp/experience.html", {"experience_data":experience_data})


class NewsView(View):
    def get(self, request, *args, **kwargs):
        news_data = NewsModel.objects.all()
        return render(request, "myapp/news.html", {"news_data":news_data})