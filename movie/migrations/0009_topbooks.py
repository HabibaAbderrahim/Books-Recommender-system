# Generated by Django 3.0.6 on 2020-06-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20200613_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(db_column='Book', max_length=100)),
                ('top1', models.CharField(db_column='Top1', max_length=100)),
                ('top2', models.CharField(db_column='Top2', max_length=100)),
                ('top3', models.CharField(db_column='Top3', max_length=100)),
            ],
            options={
                'db_table': 'top_books',
                'managed': True,
            },
        ),
    ]
