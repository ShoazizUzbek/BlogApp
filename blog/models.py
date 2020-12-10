from django.conf import settings
from django.db import models


from django.utils.translation import gettext_lazy as _


class Language(models.TextChoices):
    UZ = "UZ", _("Uzbek")
    RU = "RU", _("Russian")
    EN = "EN", _("English")

class New(models.Model):
    tags = models.ManyToManyField(
        "Tag",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_news",
    )
    added_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.pk}'


class NewsName(models.Model):

    language = models.CharField(
        max_length=2,
        choices=Language.choices
    )
    news = models.ForeignKey(
        New,
        on_delete=models.CASCADE,
        related_name='news_name'
    )
    title = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Description of news",
    )



class Tag(models.Model):
    pass

    def __str__(self):
        return f'id - {self.pk}'


class TagName(models.Model):


    tag = models.ForeignKey(
        "Tag",
        on_delete=models.CASCADE,
        related_name="tag_names"
    )
    name = models.CharField(max_length=155)
    language = models.CharField(
        max_length=2,
        choices=Language.choices
    )


    def __str__(self):
        return f'{self.language} - {self.name}'

