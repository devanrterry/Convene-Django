# Generated by Django 2.2.6 on 2019-12-20 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='comment date')),
                ('content', models.TextField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('outdoors', 'Outdoors'), ('entertainment', 'Entertainment'), ('food', 'Food'), ('tech', 'Tech'), ('education', 'Education'), ('health', 'Health')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Event')),
            ],
        ),
    ]
