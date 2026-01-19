from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0153_contest_allow_virtual_participation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemHarness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harness_code', models.TextField(help_text='Hidden test code compiled/run with the student submission.', verbose_name='harness code')),
                ('entry_point', models.CharField(blank=True, help_text='For Java: class name with main(). For Python: leave blank.', max_length=100, verbose_name='entry point')),
                ('skip_precompile', models.BooleanField(default=False, help_text='Enable if student code references classes/functions defined in the harness. The harness grader will handle compilation instead.', verbose_name='skip pre-compilation')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.language', verbose_name='language')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harnesses', to='judge.problem', verbose_name='problem')),
            ],
            options={
                'verbose_name': 'problem harness',
                'verbose_name_plural': 'problem harnesses',
                'unique_together': {('problem', 'language')},
            },
        ),
    ]
