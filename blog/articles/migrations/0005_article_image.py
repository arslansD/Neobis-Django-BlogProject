# Generated by Django 3.0.2 on 2020-01-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='kjhlhj', width_field=200),
        ),
    ]