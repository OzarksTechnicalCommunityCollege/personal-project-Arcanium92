from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('game_review', '0007_alter_gamereview_like_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='game_review.gamereview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='reviewlike',
            index=models.Index(fields=['created'], name='reviewlike_created_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='reviewlike',
            unique_together={('user', 'review')},
        ),
    ]