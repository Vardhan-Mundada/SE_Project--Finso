# Generated by Django 5.0.2 on 2024-03-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finso_app', '0002_category_alter_expense_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='budget_limit',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]