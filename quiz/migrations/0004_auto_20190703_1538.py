# Generated by Django 2.2.3 on 2019-07-03 10:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190703_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='question date'),
        ),
    ]
