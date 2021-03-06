from django.db import models
from django.utils import timezone


class Category(models.Model):
	objects = None
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.name


class TodoList(models.Model):
	objects = None
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True)
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)  # a foreignkey # a foreignkey

	class Meta:
		ordering = ["-created"]

	def __str__(self):
		return self.title


# class Categorydef(object):
# 	pass