from django.apps import AppConfig

class GameReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game_review'

# Signals
class GameReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game_review'

    def ready(self):
        import game_review.signals