from django.contrib import admin
from myapp.models import ImageModel, SkillModel, MyScenarioModel, ArtModel
# Register your models here.


@admin.register(ImageModel)
class ImagePost(admin.ModelAdmin):
    pass


@admin.register(SkillModel)
class SkillPost(admin.ModelAdmin):
    pass


@admin.register(MyScenarioModel)
class ScenarioPost(admin.ModelAdmin):
    pass


@admin.register(ArtModel)
class ArtPost(admin.ModelAdmin):
    pass
