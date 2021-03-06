# Generated by Django 2.2.10 on 2020-02-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='subject',
            field=models.CharField(blank=True, choices=[('Business', 'Business'), ('CoursePythonI', 'Course: Python I'), ('CoursePythonOOP', 'Course: Python OOP'), ('CourseMktDigital', 'Course: Mkt Digital'), ('CourseFlask', 'Course: Python Flask'), ('Q&A', 'Q&A'), ('R&S', 'R&S')], db_column='subject', db_index=True, default=6, max_length=20, null=True, verbose_name='subject'),
        ),
    ]
