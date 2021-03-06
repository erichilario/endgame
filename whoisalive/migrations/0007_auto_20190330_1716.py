# Generated by Django 2.1.7 on 2019-03-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoisalive', '0006_auto_20190329_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_desc',
            field=models.TextField(default='Description', max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='hero_image',
            field=models.ImageField(default='static/whoisalive/images/default.png', upload_to='static/whoisalive/images'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='hero_name',
            field=models.CharField(default="The Hero's Name", max_length=50),
        ),
    ]
