from django.db import models

class PresentCat(models.Model):
	id = models.AutoField(primary_key=True)
	presents_cat = models.CharField(max_length=30, null=True, blank=True, verbose_name = 'Category of present')
	def __str__(self):
		return self.presents_cat

class Present(models.Model):
	id = models.AutoField(primary_key=True)
	presents_cat = models.ForeignKey(PresentCat, on_delete=models.CASCADE,)
	present = models.CharField(max_length=30, null=True, blank=True, verbose_name = 'Name')
	price = models.IntegerField(null=True, blank=True, verbose_name = 'Price')
	class Meta:
		verbose_name = 'Present'
		verbose_name_plural = 'Presents'
	def __str__(self):
		return self.present


class User(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.CharField(max_length=300, null=True, blank=True)	
	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'

	def __str__(self):
		return self.user


class Answer(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	result_quantity = models.CharField(max_length=50,null=True, blank=True)
	result_price = models.CharField(max_length=50,null=True, blank=True)
	result_budget = models.CharField(max_length=50,null=True, blank=True)
	result_content = models.CharField(max_length=50,null=True, blank=True)
	present = models.CharField(max_length=50,null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.result

	def __str__(self):
		return f"Answer by {self.user.user}: {self.result_quantity}, {self.result_price}, {self.result_budget}, {self.result_content}. So it shows {self.present}"

	class Meta:
		ordering = ['-created']
		indexes = [
		models.Index(fields=['-created']),
		]
		verbose_name = 'Result of quiz'
		verbose_name_plural = 'Results of quiz'