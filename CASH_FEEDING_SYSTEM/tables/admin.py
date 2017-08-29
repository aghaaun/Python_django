# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Type, Note, NoteInstance, User
# Register your models here.


#admin.site.register(User)
#Defining the user login
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth')
    fields = ['first_name','last_name',('date_of_birth')]
admin.site.register(User,UserAdmin)
#admin.site.register(Note)
#admin.site.register(NoteInstance)
#admin.site.register(Type)

class NoteInstanceInline(admin.TabularInline):
    model = NoteInstance


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','user',)
    inlines = [NoteInstanceInline]


@admin.register(NoteInstance)
class NoteInstanceAdmin(admin.ModelAdmin):
    list_filter=('status','due_date')
    fieldsets = (
        (None, {
            'fields': ('note','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_date')
        }),
    )