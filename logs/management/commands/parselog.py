from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from logs.management.commands._logparser import parse
from logs.models import Category, Log


class Command(BaseCommand):
    help = 'Parse log file and insert into database'

    def add_arguments(self, parser):
        parser.add_argument('logfile', type=str, help="Log file name")

        # Named (optional) arguments
        parser.add_argument(
            '-a',
            '--append',
            action='store_true',
            help='Append to existing database',
        )

    def handle(self, *args, **options):
        logfile = options['logfile']

        self.stdout.write("Parsing log file: {}".format(logfile))

        result = parse(logfile)

        # clear previous database entries
        if not options['append']:
            Category.objects.all().delete()
            Log.objects.all().delete()

        for ts, cat, msg in result:
            category, created = Category.objects.get_or_create(name=cat)

            # parse timestamp string
            _format = "%b %d %H:%M:%S"
            parsed_datetime = make_aware(datetime.strptime(ts, _format))

            stripped_msg = ' '.join([x for x in msg.split(' ') if len(x) > 0])

            Log(
                timestamp=parsed_datetime,
                message=stripped_msg,
                category=category
            ).save()

            self.stdout.write(self.style.SUCCESS(f"[{ts}] {category} {stripped_msg} inserted."))

        self.stdout.write(self.style.SUCCESS('Successfully parsed log'))
