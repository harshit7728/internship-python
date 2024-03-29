# Generated by Django 5.0 on 2023-12-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudop', '0002_alter_student_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=227, null='True', verbose_name='student email'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, null='True', verbose_name='student name'),
        ),
    ]
