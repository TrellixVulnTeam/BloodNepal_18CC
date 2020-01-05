# Generated by Django 3.0.2 on 2020-01-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nepal_blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(default='', max_length=50)),
                ('phoneNo', models.IntegerField(default='')),
                ('email', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('bloodGroup', models.CharField(max_length=5)),
                ('RH_type', models.CharField(max_length=5)),
            ],
        ),
    ]