# Generated by Django 3.1.7 on 2023-03-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_testonomials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testonomials',
            name='post',
        ),
        migrations.AddField(
            model_name='testonomials',
            name='rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testonomials',
            name='name',
            field=models.CharField(default='Person Name', max_length=100),
        ),
    ]
