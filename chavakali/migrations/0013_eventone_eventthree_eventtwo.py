# Generated by Django 2.2.2 on 2019-07-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chavakali', '0012_bishop_reverend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Eventthree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Eventtwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]
