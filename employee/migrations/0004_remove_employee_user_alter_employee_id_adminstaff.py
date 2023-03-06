# Generated by Django 4.0.4 on 2023-03-04 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='0e4a0518-519b-4074-9a80-d9821f0de2fd', max_length=60, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.CreateModel(
            name='AdminStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]