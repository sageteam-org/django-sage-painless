from django.core.management.base import BaseCommand

from generator.services.admin_generator import AdminGenerator


class Command(BaseCommand):
    help = 'Generate admin.py for given app'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--app', type=str, help='app label that will generate admin.py for')
        parser.add_argument('-d', '--diagram', type=str, help='diagram that will generate admin.py for')

    def handle(self, *args, **options):
        app_label = options.get('app')
        diagram_path = options.get('diagram')
        admin_generator = AdminGenerator(app_label)
        generated, message = admin_generator.generate(diagram_path)
        if generated:
            self.stdout.write(
                self.style.SUCCESS(message)
            )
        else:
            self.stdout.write(
                self.style.ERROR(message)
            )
