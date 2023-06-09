# Generated by Django 4.2.1 on 2023-05-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('salery', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
