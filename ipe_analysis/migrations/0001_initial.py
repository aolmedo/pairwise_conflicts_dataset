# Generated by Django 3.2 on 2022-05-04 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pairwise_conflict_dataset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectIPEStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tw_size', models.PositiveIntegerField(verbose_name='time window size')),
                ('tw_quantity', models.PositiveIntegerField(verbose_name='# time windows')),
                ('tw_with_pc_percentage', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='% time windows with pairwise conflicts')),
                ('hist_tw_without_pc', models.ImageField(blank=True, null=True, upload_to='hist_tw_without_pc')),
                ('hist_tw_with_pc', models.ImageField(blank=True, null=True, upload_to='hist_tw_with_pc')),
                ('corr_matrix_tw_with_pc', models.ImageField(blank=True, null=True, upload_to='corr_matrix_tw_with_pc')),
                ('cov_matrix_tw_with_pc', models.ImageField(blank=True, null=True, upload_to='cov_matrix_tw_with_pc')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ipe_stats', to='pairwise_conflict_dataset.project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'project IPE stats',
                'verbose_name_plural': 'projects IPE stats',
                'ordering': ['project__created_at', 'tw_size'],
            },
        ),
        migrations.CreateModel(
            name='IPETimeWindow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('pull_requests_number', models.PositiveIntegerField(verbose_name='# merged PRs')),
                ('pairwise_conflicts_number', models.PositiveIntegerField(verbose_name='# pairwise conflicts')),
                ('potential_conflict_resolutions_number', models.PositiveIntegerField(verbose_name='# potential conflict resolutions')),
                ('unconflicting_pull_request_groups_number', models.PositiveIntegerField(verbose_name='# unconflicting PR groups')),
                ('historical_conflict_resolutions_number', models.PositiveIntegerField(verbose_name='# historical conflict resolutions')),
                ('historical_ipe', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='historical IPE ')),
                ('optimized_conflict_resolutions_number', models.PositiveIntegerField(verbose_name='# optimized conflict resolutions')),
                ('optimized_ipe', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='optimized IPE')),
                ('ipe_improvement_percentage', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IPE improvement (%)')),
                ('pairwise_conflict_graph_image', models.ImageField(blank=True, null=True, upload_to='pairwise_conflict_graphs')),
                ('colored_pairwise_conflict_graph_image', models.ImageField(blank=True, null=True, upload_to='colored_pairwise_conflict_graphs')),
                ('pull_request_group_graph_image', models.ImageField(blank=True, null=True, upload_to='pull_request_group_graphs')),
                ('integration_trajectories_image', models.ImageField(blank=True, null=True, upload_to='integration_trajectories_figures')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ipe_time_windows', to='pairwise_conflict_dataset.project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'IPE time window',
                'verbose_name_plural': 'IPE time windows',
                'ordering': ['start_date'],
            },
        ),
    ]
