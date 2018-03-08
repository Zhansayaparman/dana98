# Generated by Django 2.0.2 on 2018-02-19 07:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mugalim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Mamandyk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text=' ', max_length=1000)),
                ('isbn', models.CharField(help_text='  ', max_length=5, verbose_name='ISBN')),
                ('mugalim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Mugalim')),
            ],
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text=' ', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'bir'), ('2', 'eki'), ('3', 'ush'), ('4', 'tort')], default='m', help_text='Mamandyk availability', max_length=1)),
                ('mamandyk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Mamandyk')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' ', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='mamandyk',
            name='kafedra',
            field=models.ManyToManyField(help_text=' ', to='catalog.Kafedra'),
        ),
    ]
