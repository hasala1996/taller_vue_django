# Generated by Django 4.0.1 on 2022-01-05 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_rename_name_book_nameauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='nameAuthor',
            field=models.ForeignKey(blank=True, db_column='id_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.author', verbose_name='id del autor el cual está asociado'),
        ),
    ]
