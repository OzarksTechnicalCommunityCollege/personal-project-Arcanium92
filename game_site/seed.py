import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_site.settings')
django.setup()


from charts.models import ReviewRating

ReviewRating.objects.all().delete()

sample_data = [
    ('Borderlands 3', 8),
    ('Anthem', 3),
    ('Legend of Zelda: Tears of the Kingdom', 9),
    ('World of Warcraft', 8),
    ('Animal Crossing', 8),
]

for gameName, rating in sample_data:
    ReviewRating.objects.create(gameName=gameName, rating=rating)

print(f'Created {len(sample_data)} records.')