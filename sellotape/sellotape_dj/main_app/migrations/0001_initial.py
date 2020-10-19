# Generated by Django 3.1.1 on 2020-10-12 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('country', models.CharField(default='Israel', max_length=100)),
                ('youtube_link', models.URLField(blank=True)),
                ('twitch_link', models.URLField(blank=True)),
                ('city', models.IntegerField(choices=[(1, 'Tel Aviv'), (2, 'HaMerkaz'), (3, 'HaDarom'), (4, 'HaTzafon')], default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('airs_on', models.DateTimeField()),
                ('ends_on', models.DateTimeField(blank=True, null=True)),
                ('added_on', models.DateTimeField()),
                ('genre', models.CharField(choices=[('D', 'DIY'), ('F', 'Fashion'), ('G', 'Games'), ('C', 'Comedy'), ('T', 'Tech'), ('S', 'Podcast')], default='S', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
            options={
                'db_table': 'streams',
                'ordering': ['airs_on', '-added_on', 'genre', 'author'],
            },
        ),
        migrations.CreateModel(
            name='UserFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='main_app.profile')),
            ],
            options={
                'unique_together': {('user', 'follows')},
            },
        ),
    ]
