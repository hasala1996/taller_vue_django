# Generated by Django 4.0.1 on 2022-01-05 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateTimeField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.ForeignKey(blank=True, db_column='name', null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.author', verbose_name='id del autor el cual está asociado'),
        ),
    ]