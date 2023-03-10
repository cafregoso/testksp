# Generated by Django 4.0.4 on 2023-03-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='9591b794-bc88-4b74-b24a-06670d861e35', max_length=60, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='employees_photos', verbose_name='Photo'),
        ),
    ]
