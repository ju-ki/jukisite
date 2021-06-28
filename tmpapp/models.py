from django.db import models

# Create your models here.

GENDER = (("man", "male"), ("woman", "female"))


class TestModel(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    subtitle = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, default="Please input your name")
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)

    def __str__(self) -> str:
        return self.title


class ImageModel(models.Model):
    background_image = models.ImageField(upload_to="img/upload")
    description = models.TextField(
        max_length=200, default="This is my favorite photo")
    profile_image = models.ImageField(upload_to="img/upload", blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    kaggle = models.CharField(max_length=100, blank=True)
    signate = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=100, blank=True)


period_choice = (("一ヶ月程度", "一ヶ月程度"), ("二ヶ月から三ヶ月程", "二ヶ月から三ヶ月程"),
                 ("半年程", "半年程"), ("一年程", "一年程"))


class SkillModel(models.Model):
    language = models.CharField(max_length=20, blank=True)
    period = models.CharField(
        max_length=20, blank=True, choices=period_choice)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self) -> str:
        return self.language


class MyScenarioModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(
        max_length=10000, default="Please input text")

    def __str__(self) -> str:
        return self.title


class ArtModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    summary = models.TextField(max_length=300, blank=True)
    script = models.TextField(max_length=10000, blank=True)

    def __str__(self) -> str:
        return self.title
