# Generated by Django 3.1 on 2020-08-23 13:55

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_id', models.IntegerField(unique=True)),
                ('subj_name', models.TextField(max_length=20)),
                ('category1', models.TextField(max_length=10)),
                ('category2', models.TextField(max_length=10)),
                ('prof_name', models.TextField(max_length=10)),
                ('grading', models.TextField(max_length=100)),
                ('time', models.TextField(max_length=20)),
                ('room', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_id', models.IntegerField()),
                ('keyword', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_id', models.IntegerField()),
                ('keyword_id', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.TextField(max_length=20)),
                ('username', models.TextField(max_length=20)),
                ('user_number', models.TextField(max_length=10)),
                ('mbti', models.TextField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('keyword_id', models.IntegerField()),
                ('keyword', models.TextField(max_length=10)),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('subj_id', models.IntegerField()),
                ('good', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('subj_id', models.IntegerField()),
            ],
        ),
    ]
