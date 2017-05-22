from django.core.management.base import BaseCommand, CommandError
from course_picker.models import Professor, Course, Session
import random
from datetime import datetime
import lorem

class Command(BaseCommand):
    help = 'Populates the database with lots of sample courses'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        count = options['count'][0]
        for course_count in range(0,count):
            sentence = lorem.sentence()
            professor_name = sentence.split()[0]
            course_name = ' '.join(sentence.split()[1:])
            professor = Professor(name=professor_name)
            professor.save()
            course = Course(name=course_name, cost=random.randint(1,15000), description=lorem.paragraph())
            course.save()
            professor.courses.add(course)
            year = random.randint(1950, 2000)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            hour = random.randint(0,22)
            start_time = datetime(year, month, day, hour)
            end_time = datetime(year, month, day, hour+1)
            session = Session(start_time=start_time, end_time=end_time, course=course)
            session.save()
        self.stdout.write(self.style.SUCCESS('Successfully added %d courses' % count))