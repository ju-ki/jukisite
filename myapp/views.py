from django.shortcuts import render
from django.views.generic import View
from .models import ImageModel, SkillModel, MyScenarioModel, ArtModel


class IndexView(View):
    """top page view"""

    def get(self, request, *args, **kwargs):
        tmp_data = ImageModel.objects.all()
        skill_data = SkillModel.objects.all()
        about_data = MyScenarioModel.objects.all()
        art_data = ArtModel.objects.all()
        return render(request, "myapp/template.html",
                      {"tmp_data": tmp_data, "skill_data": skill_data,
                       "about_data": about_data, "art_data": art_data})
