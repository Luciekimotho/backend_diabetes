# Generated by Django 2.0 on 2018-02-01 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0003_auto_20180201_0548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='user',
        ),
        migrations.AddField(
            model_name='reading',
            name='patient',
            field=models.ForeignKey(default='lulu', on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='diabetes.Profile'),
            preserve_default=False,
        ),
    ]
