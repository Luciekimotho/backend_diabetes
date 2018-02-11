# Generated by Django 2.0 on 2018-02-01 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0006_auto_20180201_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='user',
        ),
        migrations.AddField(
            model_name='reading',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='diabetes.Profile'),
            preserve_default=False,
        ),
    ]
