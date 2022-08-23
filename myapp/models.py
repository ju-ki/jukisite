from django.db import models
# Create your models here.


class ImageModel(models.Model):
    background_image = models.ImageField(upload_to="img/upload", blank=True)
    description = models.TextField(
        max_length=200, default="Welcome to my site!!")
    profile_image = models.ImageField(upload_to="img/upload", blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    kaggle = models.CharField(max_length=100, blank=True)
    signate = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=100, blank=True)


period_choice = (("一ヶ月程度", "一ヶ月程度"), ("二ヶ月から三ヶ月程", "二ヶ月から三ヶ月程"),
                 ("半年程", "半年程"), ("一年程", "一年程"))


class ContactModel(models.Model):
    email = models.EmailField(max_length=50, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)


class SkillModel(models.Model):
    language = models.CharField(max_length=20, blank=True)
    period = models.CharField(
        max_length=20, blank=True, choices=period_choice)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self) -> str:
        return self.language


class IntroductionModel(models.Model):
    summary = models.TextField(max_length=300, blank=True)
    script = models.CharField(max_length=300, blank=True, null=True)
    name = models.TextField(max_length=200, blank=True)


class SelfIntroductionModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(
        max_length=10000, default="Please input text")

    def __str__(self) -> str:
        return self.title


class BlogModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    summary = models.TextField(max_length=300, blank=True)
    url = models.URLField(blank=True)
    script = models.TextField(max_length=10000, blank=True)

    def __str__(self) -> str:
        return self.title


class ExperienceModel(models.Model):
    summary = models.TextField(max_length=300, blank=True)
    url = models.URLField(blank=True)


class NewsModel(models.Model):
    news = models.TextField(max_length=200, blank=True)