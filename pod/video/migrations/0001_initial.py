# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-18 01:24
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import pod.video.models
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('authentication', '0001_initial'),
        ('filepicker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('title_nl_NL', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Used to access this instance, the "slug" is a short label containing only letters, numbers, underscore or dash top.', max_length=100, unique=True, verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Description')),
                ('description_fr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('description_nl_NL', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('color', models.CharField(blank=True, max_length=10, null=True, verbose_name='Background color')),
                ('style', models.TextField(blank=True, null=True, verbose_name='Extra style')),
                ('visible', models.BooleanField(default=False, help_text='If checked, the channel appear in a list of available channels on the platform.', verbose_name='Visible')),
                ('headband', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filepicker.CustomImageModel', verbose_name='Headband')),
                ('owners', models.ManyToManyField(blank=True, related_name='owners_channels', to='authentication.Owner', verbose_name='Owners')),
                ('users', models.ManyToManyField(blank=True, related_name='users_channels', to='authentication.Owner', verbose_name='Users')),
            ],
            options={
                'verbose_name_plural': 'Channels',
                'verbose_name': 'Channel',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('title_fr', models.CharField(max_length=100, null=True, unique=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=100, null=True, unique=True, verbose_name='title')),
                ('title_nl_NL', models.CharField(max_length=100, null=True, unique=True, verbose_name='title')),
                ('slug', models.SlugField(help_text='Used to access this instance, the "slug" is a short label containing only letters, numbers, underscore or dash top.', max_length=100, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_nl_NL', models.TextField(blank=True, null=True)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filepicker.CustomImageModel', verbose_name='Icon')),
            ],
            options={
                'verbose_name_plural': 'Disciplines',
                'verbose_name': 'Discipline',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='EncodingAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('audio', 'audio'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('playlist', 'playlist')], default='360p', max_length=10, verbose_name='Name')),
                ('encoding_format', models.CharField(choices=[('video/mp4', 'video/mp4'), ('video/mp2t', 'video/mp2t'), ('video/webm', 'video/webm'), ('audio/mp3', 'audio/mp3'), ('audio/wav', 'audio/wav'), ('application/x-mpegURL', 'application/x-mpegURL')], default='video/mp4', max_length=22, verbose_name='Format')),
                ('source_file', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='encoding source file')),
            ],
        ),
        migrations.CreateModel(
            name='EncodingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EncodingVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('audio', 'audio'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('playlist', 'playlist')], default='360p', max_length=10, verbose_name='Name')),
                ('encoding_format', models.CharField(choices=[('video/mp4', 'video/mp4'), ('video/mp2t', 'video/mp2t'), ('video/webm', 'video/webm'), ('audio/mp3', 'audio/mp3'), ('audio/wav', 'audio/wav'), ('application/x-mpegURL', 'application/x-mpegURL')], default='video/mp4', max_length=22, verbose_name='Format')),
                ('source_file', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='encoding source file')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistM3U8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('audio', 'audio'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('playlist', 'playlist')], default='360p', max_length=10, verbose_name='Name')),
                ('encoding_format', models.CharField(choices=[('video/mp4', 'video/mp4'), ('video/mp2t', 'video/mp2t'), ('video/webm', 'video/webm'), ('audio/mp3', 'audio/mp3'), ('audio/wav', 'audio/wav'), ('application/x-mpegURL', 'application/x-mpegURL')], default='video/mp4', max_length=22, verbose_name='Format')),
                ('source_file', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='encoding source file')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('title_nl_NL', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Used to access this instance, the "slug" is a short label containing only letters, numbers, underscore or dash top.', max_length=100, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_nl_NL', models.TextField(blank=True, null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='video.Channel', verbose_name='Channel')),
                ('headband', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filepicker.CustomImageModel', verbose_name='Headband')),
                ('parentId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.Theme')),
            ],
            options={
                'verbose_name_plural': 'Themes',
                'verbose_name': 'Theme',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('title_nl_NL', models.CharField(max_length=100, null=True, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Used to access this instance, the "slug" is a short label containing only letters, numbers, underscore or dash top.', max_length=100, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_nl_NL', models.TextField(blank=True, null=True)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filepicker.CustomImageModel', verbose_name='Icon')),
            ],
            options={
                'verbose_name_plural': 'Types',
                'verbose_name': 'Type',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='Video')),
                ('allow_downloading', models.BooleanField(default=False, verbose_name='allow downloading')),
                ('is_360', models.BooleanField(default=False, verbose_name='video 360')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('title_nl_NL', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('slug', models.SlugField(editable=False, help_text='Used to access this instance, the "slug" is a short label containing only letters, numbers, underscore or dash top.', max_length=255, unique=True, verbose_name='Slug')),
                ('date_added', models.DateField(default=datetime.datetime.now, verbose_name='Date added')),
                ('date_evt', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Date of event')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Description')),
                ('description_fr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('description_nl_NL', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('cursus', models.CharField(choices=[('0', 'None / All'), ('L', 'Bachelor’s Degree'), ('M', 'Master’s Degree'), ('D', 'Doctorate'), ('1', 'Other')], default='0', max_length=1, verbose_name='University course')),
                ('main_lang', models.CharField(choices=[('fr', 'French')], default='fr', max_length=2, verbose_name='Main language')),
                ('duration', models.IntegerField(blank=True, default=0, editable=False, verbose_name='Duration')),
                ('is_draft', models.BooleanField(default=True, help_text='If this box is checked, the video will be visible and accessible only by you.', verbose_name='Draft')),
                ('is_restricted', models.BooleanField(default=False, help_text='If this box is checked, the video will only be accessible to authenticated users.', verbose_name='Restricted access')),
                ('password', models.CharField(blank=True, help_text='Viewing this video will not be possible without this password.', max_length=50, null=True, verbose_name='password')),
                ('tags', tagging.fields.TagField(blank=True, help_text='Separate tags with spaces, enclose the tags consist of several words in quotation marks.', max_length=255, verbose_name='Tags')),
                ('overview', models.ImageField(blank=True, editable=False, max_length=255, null=True, upload_to=pod.video.models.get_upload_path_files, verbose_name='Overview')),
                ('licence', models.CharField(blank=True, choices=[('BY', 'Attribution'), ('BY ND', 'Attribution + Pas de Modification'), ('BY NC ND', 'Attribution + Pas d’Utilisation Commerciale + Pas de Modification'), ('BY NC', 'Attribution + Pas d’Utilisation Commerciale'), ('BY NC SA', 'Attribution + Pas d’Utilisation Commerciale + Partage dans les mêmes conditions'), ('BY SA', 'Attribution + Partage dans les mêmes conditions')], max_length=8, null=True, verbose_name='Licence')),
                ('encoding_in_progress', models.BooleanField(default=False, editable=False, verbose_name='Encoding in progress')),
                ('encoding_step', models.CharField(blank=True, max_length=50, null=True, verbose_name='Encoding step')),
                ('channel', models.ManyToManyField(blank=True, to='video.Channel', verbose_name='Channels')),
                ('discipline', models.ManyToManyField(blank=True, to='video.Discipline', verbose_name='Disciplines')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Owner', verbose_name='Owner')),
                ('restrict_access_to_groups', models.ManyToManyField(blank=True, help_text='Select one or more groups who can access to this video', to='auth.Group', verbose_name='Goups')),
                ('theme', models.ManyToManyField(blank=True, to='video.Theme', verbose_name='Themes')),
                ('thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filepicker.CustomImageModel', verbose_name='Thumbnails')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video.Type', verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='VideoImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=pod.video.models.get_upload_path_files, verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='VideoRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(help_text='Please use the only format x. i.e.: <em>640x360</em> or <em>1280x720</em> or <em>1920x1080</em>.', max_length=250, verbose_name='resolution')),
                ('video_bitrate', models.CharField(help_text='Please use the only format k. i.e.: <em>300k</em> or <em>600k</em> or <em>1000k</em>.', max_length=250, verbose_name='bitrate video')),
                ('audio_bitrate', models.CharField(help_text='Please use the only format k. i.e.: <em>300k</em> or <em>600k</em> or <em>1000k</em>.', max_length=250, verbose_name='bitrate audio')),
                ('encode_mp4', models.BooleanField(default=False, verbose_name='Make a MP4 version')),
            ],
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Date')),
                ('count', models.IntegerField(default=0, editable=False, verbose_name='Number of view')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='Video')),
            ],
        ),
        migrations.AddField(
            model_name='playlistm3u8',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='encodingvideo',
            name='rendition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.VideoRendition', verbose_name='rendition'),
        ),
        migrations.AddField(
            model_name='encodingvideo',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='encodinglog',
            name='video',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='encodingaudio',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='Video'),
        ),
    ]
