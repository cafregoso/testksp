# Generated by Django 4.0.4 on 2023-03-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='e01128ac-bc37-477e-83ad-2e5d9d8809f2', max_length=60, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
