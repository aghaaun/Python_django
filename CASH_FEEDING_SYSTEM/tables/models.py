# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
import uuid

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200, help_text = "Enter the note type(example etc.)")

    def __str__(self):
        """
        String for representing the model object in admin site
        """
        return self.name



class Note(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('User',on_delete=models.SET_NULL, null = True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief descriptions')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    type = models.ManyToManyField(Type, help_text="Select a type for this book")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail',args=[str(self.isbn)])
import uuid
class NoteInstance(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4, help_text = "Unique ID for this particular Note across whole system")
    note = models.ForeignKey('Note', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null = True, blank = True)

    NOTES_STATUS = (
        ('m','Maintanance'),
        ('d','Damaged'),
        ('a','Available'),
    )

    status = models.CharField(max_length=1,choices=NOTES_STATUS,blank=True,
    default='a', help_text='Note availability')

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        """
        String for reprsenting the models object
        """
        return '%s (%s)' % (self.id)#self.note.title)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    
    def get_absolute_url(self):
        """
        Returning the url to access a particular author intance
        """
        return reverse('user-detail',args=[str(self.id)])
    def __str__(self):
        """
        String for representating the model object
        """
        return '%s (%s)'% (self.last_name, self.first_name)











