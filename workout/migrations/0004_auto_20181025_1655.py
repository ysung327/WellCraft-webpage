# Generated by Django 2.1 on 2018-10-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_auto_20181025_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['monday']},
        ),
        migrations.AlterField(
            model_name='workoutinfo',
            name='how',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]