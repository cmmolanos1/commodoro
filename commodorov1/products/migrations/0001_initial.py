# Generated by Django 3.0.3 on 2020-03-02 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('variety', models.CharField(max_length=50)),
                ('processing', models.CharField(max_length=50)),
                ('crop_year', models.IntegerField()),
                ('couping_score', models.IntegerField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_coffee', to='places.Farm')),
            ],
        ),
    ]