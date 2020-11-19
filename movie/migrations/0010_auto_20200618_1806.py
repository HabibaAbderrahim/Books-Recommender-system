# Generated by Django 3.0.6 on 2020-06-18 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_topbooks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topbooks',
            name='id',
        ),
        migrations.AddField(
            model_name='topbooks',
            name='id_tops',
            field=models.AutoField(db_column='id_Tops', default='', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topbooks',
            name='book',
            field=models.ForeignKey(db_column='Book', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
    ]
