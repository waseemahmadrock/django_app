# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-13 05:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=254)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_commneted', models.CharField(blank=True, max_length=256, null=True)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('body', models.TextField(max_length=254)),
                ('user_posted', models.CharField(blank=True, max_length=254, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('userpost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unliked_date', models.DateTimeField(auto_now_add=True)),
                ('unliked_post', models.ManyToManyField(blank=True, null=True, to='fOn.Post')),
                ('userunlike', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms,')], max_length=3)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('friends', models.ManyToManyField(related_name='_userdetail_friends_+', to='fOn.UserDetail')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='liked_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fOn.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='userlike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fOn.Post'),
        ),
    ]