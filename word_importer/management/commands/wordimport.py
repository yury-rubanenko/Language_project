from django.core.management.base import BaseCommand
from platforms.models import Word
import csv
import ipdb

class Command(BaseCommand):
    help = "import new words CSV.files"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    
    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                word = row[0]
                translation = row[1]
                language = row[3]

                Word.objects.create(
                    word=word,
                    translation=translation,
                    language=language
                )

                self.stdout.write(self.style.SUCCESS(f'Successfully added word: {word}'))

