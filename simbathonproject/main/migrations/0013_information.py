# Generated by Django 5.0.6 on 2024-06-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_custom_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=20, null=True)),
                ('major', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]