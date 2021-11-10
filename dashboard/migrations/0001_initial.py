# Generated by Django 3.2.5 on 2021-08-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=255, verbose_name='Функция')),
                ('graph', models.ImageField(blank=True, null=True, upload_to='graphs/', verbose_name='График')),
                ('interval', models.IntegerField(verbose_name='Интервал')),
                ('dt', models.IntegerField(verbose_name='Шаг')),
                ('processing_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата обработки')),
            ],
        ),
    ]