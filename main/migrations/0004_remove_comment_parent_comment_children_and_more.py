# Generated by Django 4.0.7 on 2022-10-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment_parent_alter_comment_post_alter_comment_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='children',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_%(class)s', to='main.comment', verbose_name='Дочерний комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name=''),
        ),
    ]
