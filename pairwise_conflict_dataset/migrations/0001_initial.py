# Generated by Django 3.2 on 2022-05-04 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghtorrent_id', models.PositiveIntegerField(verbose_name='GHTorrent ID')),
                ('sha', models.CharField(max_length=40, verbose_name='sha')),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('raw_data', models.JSONField(verbose_name='raw data')),
            ],
            options={
                'verbose_name': 'commit',
                'verbose_name_plural': 'commits',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghtorrent_id', models.PositiveIntegerField(verbose_name='GHTorrent ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('github_url', models.URLField(verbose_name='github url')),
                ('api_url', models.URLField(verbose_name='github api url')),
                ('language', models.CharField(max_length=255, verbose_name='language')),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('default_branch', models.CharField(blank=True, max_length=255, null=True, verbose_name='default branch')),
                ('pairwise_conflicts_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='pairwise conflict count')),
                ('data_quality_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='data quality (%)')),
                ('raw_data', models.JSONField(verbose_name='raw data')),
                ('github_raw_data', models.JSONField(blank=True, null=True, verbose_name='github raw data')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghtorrent_id', models.PositiveIntegerField(verbose_name='GHTorrent ID')),
                ('github_id', models.PositiveIntegerField(verbose_name='github id')),
                ('intra_branch', models.BooleanField(verbose_name='is intra branch?')),
                ('merged', models.BooleanField(verbose_name='is merged?')),
                ('opened_at', models.DateTimeField(verbose_name='opened at')),
                ('closed_at', models.DateTimeField(blank=True, null=True, verbose_name='closed at')),
                ('base_branch', models.CharField(blank=True, max_length=255, null=True, verbose_name='target branch')),
                ('raw_data', models.JSONField(verbose_name='raw data')),
                ('github_raw_data', models.JSONField(blank=True, null=True, verbose_name='github raw data')),
                ('base_commit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='base_pull_requests', to='pairwise_conflict_dataset.commit', verbose_name='base commit')),
                ('head_commit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='head_pull_requests', to='pairwise_conflict_dataset.commit', verbose_name='head commit')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pull_requests', to='pairwise_conflict_dataset.project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'pull request',
                'verbose_name_plural': 'pull requests',
                'ordering': ['opened_at'],
            },
        ),
        migrations.CreateModel(
            name='PairwiseConflict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_pull_request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_pairwise_conflicts', to='pairwise_conflict_dataset.pullrequest', verbose_name='first pull request')),
                ('second_pull_request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_pairwise_conflicts', to='pairwise_conflict_dataset.pullrequest', verbose_name='second pull request')),
            ],
            options={
                'verbose_name': 'pairwise conflict',
                'verbose_name_plural': 'pairwise conflicts',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commits', to='pairwise_conflict_dataset.project', verbose_name='project'),
        ),
    ]
