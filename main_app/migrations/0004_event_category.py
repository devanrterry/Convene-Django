from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('outdoors', 'Outdoors'), ('entertainment', 'Entertainment'), ('food', 'Food'), ('tech', 'Tech'), ('education', 'Education'), ('health', 'Health')], default='', max_length=100),
        ),
    ]
