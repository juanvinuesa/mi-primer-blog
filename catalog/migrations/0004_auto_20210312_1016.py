# Generated by Django 2.2.18 on 2021-03-12 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Autor'),
        ),
        migrations.AddField(
            model_name='libro',
            name='isbn',
            field=models.CharField(default='', max_length=13, verbose_name='ISBN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='palabras',
            field=models.ManyToManyField(to='catalog.Claves'),
        ),
    ]
