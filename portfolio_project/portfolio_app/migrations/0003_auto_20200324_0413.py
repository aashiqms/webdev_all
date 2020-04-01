# Generated by Django 3.0.4 on 2020-03-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_remove_otherusers_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='OtherUsers',
        ),
    ]