# Generated by Django 3.0.3 on 2020-03-10 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmName', models.CharField(max_length=50)),
                ('profilePic', models.ImageField(default='default.jpg', upload_to='assets/img')),
                ('bio', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('facebook', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='farm_pics')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_picture', to='places.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('milestone', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=25)),
                ('comment', models.TextField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_history', to='places.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_certificate', to='places.Farm')),
            ],
        ),
    ]
