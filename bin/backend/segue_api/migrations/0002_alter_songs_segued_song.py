# Generated by Django 4.0.4 on 2023-07-14 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('segue_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='segued_song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='segue_api.songs'),
        ),
    ]
