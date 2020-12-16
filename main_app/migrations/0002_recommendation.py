# Generated by Django 3.1.4 on 2020-12-16 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
                ('city', models.CharField(choices=[('LA', 'Los Angeles'), ('SF', 'San Francisco'), ('P', 'Portland'), ('S', 'Seattle')], default='LA', max_length=2)),
                ('description', models.TextField(max_length=250)),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
    ]