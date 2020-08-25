import os,random
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'mytest.settings')
django.setup()
from django.contrib.auth.models import User
from faker import Faker
from testing.models import *

def create_staff(N):
	fake=Faker()
	for x in range(1,N+1):
		print(x)
		Staff.objects.create(user=User.objects.get(id=x),staff_no=x)
	print("****************DONE")

def create_task(N):
	fake=Faker()
	for _ in range(N):
		title=fake.name()
		desc=fake.sentence()
		staff=random.randint(1,4)
		Task.objects.create(title=title, desc=desc, staff=Staff.objects.get(staff_no=staff))

create_staff(4)
create_task(10)
print("POPULATED")