from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Staff(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="staff")
	staff_no=models.IntegerField(primary_key=True)

	def __str__(self):
		return self.user.first_name

class Task(models.Model):
	STATE=((0,'pending'),(1,'in_progress'),(2,'Done'))
	title=models.CharField(max_length=10)
	desc=models.CharField(max_length=35)
	status=models.IntegerField(choices=STATE,default=0)
	staff=models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="task")

	def __str__(self):
		return self.title+" - "+str(self.staff)