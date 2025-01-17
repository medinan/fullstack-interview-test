# Generated by Django 3.1.2 on 2021-07-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('branch_base', models.CharField(max_length=100)),
                ('branch_compare', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('open', 'open'), ('closed', 'closed'), ('merged', 'merged')], default='open', max_length=50)),
            ],
        ),
    ]
