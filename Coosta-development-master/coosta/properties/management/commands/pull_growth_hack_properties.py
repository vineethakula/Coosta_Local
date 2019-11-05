from django.core.management.base import BaseCommand, CommandError
from properties.views import pull_growth_hack_properties
import datetime

class Command(BaseCommand):
    help = 'update all the email address for existing listings'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print "-----Starting Job To Pull the Emails at " + datetime.datetime.today().strftime(
            "%Y-%m-%d %H:%M:%S") + "-----"
        output = pull_growth_hack_properties()

        self.stdout.write(self.style.SUCCESS(output))
        print "-----Ending Job To Pull the Emails at " + datetime.datetime.today().strftime(
            "%Y-%m-%d %H:%M:%S") + "-----"