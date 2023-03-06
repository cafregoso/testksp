# Generated by Django 4.0.4 on 2023-03-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_alter_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='38164954-5e2b-4ffb-9b09-44fe7b4f352e', max_length=60, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]