# Generated by Django 3.0.6 on 2020-05-18 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('book_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.BookInfo')),
            ],
        ),
    ]
