# Generated by Django 2.1.7 on 2019-03-25 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trivia_text', models.CharField(max_length=200)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whoisalive.Hero', verbose_name='hero trivia')),
            ],
            options={
                'ordering': ('trivia_text',),
            },
        ),
    ]
