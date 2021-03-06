# Generated by Django 2.2.8 on 2020-08-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_nome', models.CharField(max_length=200)),
                ('test_topic', models.CharField(max_length=200)),
                ('test_sumary', models.TextField(max_length=200)),
                ('test_number', models.IntegerField(default=0)),
                ('test_test', models.BooleanField(default=True)),
            ],
        ),
    ]
