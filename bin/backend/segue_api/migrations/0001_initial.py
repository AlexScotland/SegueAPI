# Generated by Django 4.0.4 on 2023-07-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('segued_song', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='segue_api.songs')),
            ],
        ),
    ]
