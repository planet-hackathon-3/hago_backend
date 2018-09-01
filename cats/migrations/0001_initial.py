# Generated by Django 2.1.1 on 2018-09-01 08:25

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', common.models.CreationDateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('modified', common.models.ModificationDateTimeField(auto_now=True, verbose_name='수정일시')),
                ('url', models.URLField(verbose_name='이미지 URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', common.models.CreationDateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('modified', common.models.ModificationDateTimeField(auto_now=True, verbose_name='수정일시')),
                ('content', models.TextField(verbose_name='내용')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
