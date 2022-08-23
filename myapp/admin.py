from django.contrib import admin
from myapp.models import ImageModel, SkillModel, IntroductionModel, SelfIntroductionModel, BlogModel, ContactModel, ExperienceModel, NewsModel
# Register your models here.


@admin.register(ImageModel)
class ImagePost(admin.ModelAdmin):
    pass


@admin.register(SkillModel)
class SkillPost(admin.ModelAdmin):
    pass


@admin.register(ExperienceModel)
class ExperiencePost(admin.ModelAdmin):
    pass


@admin.register(BlogModel)
class BlogPost(admin.ModelAdmin):
    pass


@admin.register(IntroductionModel)
class IntroductionPost(admin.ModelAdmin):
    pass


@admin.register(SelfIntroductionModel)
class SelfIntroductionPost(admin.ModelAdmin):
    pass


@admin.register(ContactModel)
class ContactPost(admin.ModelAdmin):
    pass


@admin.register(NewsModel)
class NewsPost(admin.ModelAdmin):
    pass