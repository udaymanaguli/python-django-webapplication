from django.contrib import admin
from .models import Voter, Vote

# Register your models here.
admin.site.register(Voter)
admin.site.register(Vote)
