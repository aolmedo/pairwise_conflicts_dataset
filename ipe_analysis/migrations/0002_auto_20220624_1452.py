# Generated by Django 3.2 on 2022-06-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipe_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectipestats',
            name='corr_matrix_tw_with_pc',
        ),
        migrations.RemoveField(
            model_name='projectipestats',
            name='cov_matrix_tw_with_pc',
        ),
        migrations.RemoveField(
            model_name='projectipestats',
            name='hist_tw_with_pc',
        ),
        migrations.RemoveField(
            model_name='projectipestats',
            name='hist_tw_without_pc',
        ),
        migrations.AddField(
            model_name='ipetimewindow',
            name='cr_improvement_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='# conflict resolutions improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipetimewindow',
            name='tw_size',
            field=models.PositiveIntegerField(default=14, verbose_name='time window size'),
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='cr_improvement_percentage_max',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='MAX # CR improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='cr_improvement_percentage_mean',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='MEAN # CR improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='cr_improvement_percentage_min',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='MIN # conflict resolutions improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='cr_improvement_percentage_std',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='STD # CR improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='ipe_improvement_percentage_max',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='MAX IPE improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='ipe_improvement_percentage_mean',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='MEAN IPE improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='ipe_improvement_percentage_min',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='MIN IPE improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='ipe_improvement_percentage_std',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='STD IPE improvement (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='tw_equal_cr_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='# time windows equal CR number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='tw_equal_ipe_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='# time windows equal IPE'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='tw_improves_cr_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='# time windows improve CR number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='tw_improves_ipe_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='# time windows improve IPE'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectipestats',
            name='tw_worsen_ipe_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='# time windows not improve IPE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectipestats',
            name='tw_size',
            field=models.PositiveIntegerField(default=14, verbose_name='time window size'),
        ),
    ]
