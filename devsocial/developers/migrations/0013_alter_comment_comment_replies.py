# Generated by Django 4.2.4 on 2023-08-20 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0012_comment_comment_replies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_replies',
            field=models.ManyToManyField(blank=True, related_name='comment_replies', to='developers.post'),
        ),
    ]
