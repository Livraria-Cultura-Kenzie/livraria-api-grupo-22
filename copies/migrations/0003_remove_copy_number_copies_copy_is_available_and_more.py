# Generated by Django 4.2.2 on 2023-07-03 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_book_number_copies"),
        ("copies", "0002_copy_number_copies"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="copy",
            name="number_copies",
        ),
        migrations.AddField(
            model_name="copy",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="copy",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="copies",
                to="books.book",
            ),
        ),
    ]
