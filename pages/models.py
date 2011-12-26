from django.db import models


class Song(models.Model):
	title=models.CharField(max_length=500)
	artist=models.CharField(max_length=500)
	comment=models.TextField(blank=True)
	your_name=models.CharField(max_length=500)
	added_on=models.DateTimeField(auto_now_add=True)