# Generated by Django 3.2.20 on 2023-09-25 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_remove_expense_expense_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expense_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.account'),
        ),
    ]
