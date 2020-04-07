# Generated by Django 2.2 on 2020-03-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('chapterNum', models.IntegerField()),
                ('pageNum', models.IntegerField()),
            ],
        ),
    ]
