# Generated by Django 3.0.3 on 2020-03-10 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200310_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='farm',
            new_name='product',
        ),
    ]