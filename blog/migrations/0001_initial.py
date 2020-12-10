# Generated by Django 3.1.4 on 2020-12-10 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(verbose_name='Description of news')),
                ('add_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_news', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='TagName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('language', models.CharField(choices=[('UZ', 'Uzbek'), ('RU', 'Russian'), ('EN', 'English')], max_length=2)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_names', to='blog.tag')),
            ],
            options={
                'unique_together': {('tag', 'language')},
            },
        ),
    ]
