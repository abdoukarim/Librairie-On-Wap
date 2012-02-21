# coding: utf-8
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib import admin

from mobile.librairie.managers import AuthorOnlineManager
# Create your models here.

class Author(models.Model):
	STATUS = 0
	SELECT = 1
	STATUS_DEFAULT = STATUS
	STATUS_CHOICES = (
	(STATUS, ('Normal')),
	(SELECT, ('Selection')),
	)
	name = models.CharField(max_length=100)
	#friends = models.ManyToManyField('self', blank=True)
	contact = models.TextField(blank=True)
	description = models.TextField()
	status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DEFAULT, db_index=True)

	#objects = models.Manager()
	#online_objects = AuthorOnlineManager()

	def __unicode__(self):
		return self.name

class Publisher(models.Model):
	    name = models.CharField(max_length=255)
	    #num_awards = models.IntegerField()
	
	    def __unicode__(self):
	        return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
	        return self.name

class Theme(models.Model):
	slug = models.SlugField(max_length=255)
	monthTheme = models.BooleanField(null=False, blank=False, default=False)
	category = models.ForeignKey(Category)
	
	def __unicode__(self):
	        return self.slug
	 
	def toggle_monthTheme(self):
		return '<a href="%s">Toggle</a>' % reverse('librairie.views.toggle_monthTheme', args=[self.pk])
	toggle_monthTheme.allow_tag = True


class Livre(models.Model):
	title = models.CharField(max_length=255)
	#slug = models.SlugField(max_length=255)
	publisher = models.ForeignKey(Publisher)
	price = models.FloatField()
	pages = models.DecimalField(decimal_places=2, max_digits=6)
	height = models.DecimalField(decimal_places=2, max_digits=6)
	width = models.DecimalField(decimal_places=2, max_digits=6)
	language = models.CharField(max_length=255)
	isbn = models.CharField(max_length=12)
	resume = models.TextField()
	authors = models.ManyToManyField(Author)
	theme = models.ForeignKey(Theme)
	
	def __unicode__(self):
	        return self.title
