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
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=100)),
                ('tmdb_actor_id', models.CharField(max_length=100)),
                ('profile_path', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kmdb_id', models.CharField(max_length=100)),
                ('tmdb_id', models.CharField(max_length=100, null=True)),
                ('kmdb_seq', models.CharField(max_length=100)),
                ('movie_title', models.CharField(max_length=200)),
                ('director_name', models.CharField(max_length=100)),
                ('nation', models.CharField(max_length=100)),
                ('plot', models.TextField()),
                ('runtime', models.CharField(max_length=100)),
                ('rating', models.TextField()),
                ('release_date', models.CharField(max_length=100)),
                ('keywords', models.TextField()),
                ('poster', models.URLField()),
                ('teaser', models.URLField()),
                ('actors', models.ManyToManyField(related_name='movies_actor', to='movies.Actor')),
                ('genres', models.ManyToManyField(related_name='movies_genre', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='LocationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField()),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.location')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='movies',
            field=models.ManyToManyField(related_name='locations', through='movies.LocationDetail', to='movies.Movies'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rate', models.IntegerField()),
                ('like_users', models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
