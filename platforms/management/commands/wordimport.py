import csv

from django.core.management.base import BaseCommand

from platforms.models import Word


class Command(BaseCommand):
    help = "Import new words from CSV files"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                word = row['word']
                translation = row['translation']
                language = row['language']

                word_obj, created = Word.objects.get_or_create(
                    word=word,
                    translation=translation,
                    language=language
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added word: {word}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Word already exists: {word}'))
