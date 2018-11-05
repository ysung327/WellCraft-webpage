# Generated by Django 2.1 on 2018-10-27 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_auto_20181025_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workout_info.WorkoutInfo'),
        ),
        migrations.DeleteModel(
            name='WorkoutInfo',
        ),
    ]
