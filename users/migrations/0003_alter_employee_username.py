# Generated by Django 4.1.7 on 2023-03-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_employee_managers_alter_employee_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="username",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Username"
            ),
        ),
    ]
