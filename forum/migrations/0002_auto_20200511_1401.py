# Generated by Django 2.2.12 on 2020-05-11 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grandCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='forum.GrandCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='parentCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='forum.ParentCategory'),
            preserve_default=False,
        ),
    ]