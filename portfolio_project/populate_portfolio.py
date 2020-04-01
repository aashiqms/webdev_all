import os
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
import django
django.setup()

from portfolio_app.models import User


# fake populate script


fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        # create new entry in our actual database
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('print populating complete')



