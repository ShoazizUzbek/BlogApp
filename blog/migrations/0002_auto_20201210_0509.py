# Generated by Django 3.1.4 on 2020-12-10 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='description',
        ),
        migrations.RemoveField(
            model_name='new',
            name='title',
        ),
        migrations.CreateModel(
            name='NewsName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('UZ', 'Uzbek'), ('RU', 'Russian'), ('EN', 'English')], max_length=255, unique=True)),
                ('description', models.TextField(choices=[('UZ', 'Uzbek'), ('RU', 'Russian'), ('EN', 'English')], verbose_name='Description of news')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_name', to='blog.new')),
            ],
        ),
    ]
