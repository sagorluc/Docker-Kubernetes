# Generated by Django 5.1 on 2024-08-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_blog_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='photo/img.png', null=True, upload_to='photo/', verbose_name='Image'),
        ),
    ]
