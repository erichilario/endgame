# Generated by Django 2.1.7 on 2019-03-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoisalive', '0010_auto_20190330_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]