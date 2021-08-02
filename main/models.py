from django.db import models
from django.urls import reverse

# Create your models here.



class Category(models.Model):
	name = models.CharField('Nomi',max_length=150,)
	slug = models.SlugField('*',max_length=150, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('main:category_detail', kwargs={'category_slug':self.slug})



class Author(models.Model):
	name = models.CharField('Nomi',max_length=150,)
	slug = models.SlugField('*',max_length=150, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('main:author_detail', kwargs={'author_slug':self.slug})


class Movie(models.Model):
	title = models.CharField('Title',max_length=50,unique=True)
	slug = models.SlugField('*',max_length=50,unique=True)
	category = models.ForeignKey(Category,
		on_delete=models.CASCADE,
		related_name='posts')
	video = models.FileField('Movie', upload_to='movie_files/')
	author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author')
	date = models.DateTimeField(auto_now_add=True)
	body = models.CharField('Text',max_length=300)
	views = models.PositiveIntegerField('Korildi', default=0)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('main:movie_detail', kwargs={'movie_slug':self.slug})
