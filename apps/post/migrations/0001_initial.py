# Generated by Django 4.1.7 on 2023-03-26 13:19

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
            name='Post',
            fields=[
                ('slug', models.SlugField(max_length=127, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=127, unique=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['author', 'slug', 'title', 'content'], name='posts_author__fe5740_idx'),
        ),
    ]
