# Generated by Django 4.0.4 on 2023-03-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0024_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='0fdb4a70-5790-4c31-89fe-ab9257e7170c', max_length=60, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
