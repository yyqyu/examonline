# Generated by Django 2.1.4 on 2019-02-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testquestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestioninfo',
            name='edit_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]