# Generated by Django 4.2.1 on 2023-05-25 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=14)),
                ('price', models.IntegerField(default=0)),
                ('categorry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
