from django.db import models
from django.contrib import auth
from django.core.validators import MinValueValidator, MaxValueValidator

class Read(models.Model):
	user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, null=False)
	cover = models.CharField(max_length=200, null=False, help_text="Give an image url of the book cover")
	rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	review = models.TextField()
	date = models.DateField()
	def __str__(self):
		return "{}({})".format(self.title, self.user)
	   # cover = models.ImageField(
    #     ("Book Cover"), 
    #     upload_to='static/images/read/',
    #      max_length=None,
    #      blank = True,null = True)

class TBR(models.Model):
	user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, null=False)
	author = models.CharField(max_length=100, null=False)
	description = models.TextField()
	pub_time = models.DateTimeField(auto_now=True)
	# now = datetime.now()
	def __str__(self):
		return "{}({})".format(self.title, self.user)
	   # cover = models.ImageField(
    #     ("Book Cover"), 
    #     upload_to='static/images/read/',
    #      max_length=None,
    #      blank = True,null = True)

class Ask(models.Model):
	user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, null=False)
	description = models.TextField()
	triggers = models.TextField(help_text="Please seperate tags with commas or spaces")
	pub_time = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "{}({})".format(self.title, self.user)

class Rec(models.Model):
	ask = models.ForeignKey(Ask, on_delete=models.CASCADE)
	user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, null=False)
	author = models.CharField(max_length=100, null=False)
	description = models.TextField()
	# comment = models.TextField()
	pub_time = models.DateTimeField(auto_now=True)
	# now = datetime.now()
	def __str__(self):
		return "{}({}) for {}".format(self.title, self.user, self.ask.title)


# # Create your models here.
# class User(models.Model):
# 	name = models.CharField(max_length=20, null=False)
# 	email = models.EmailField()
# 	password = models.CharField(max_length=20, null=False)
# 	enabled = models.BooleanField(default=False)
# 	def __str__(self):
# 		return self.name

