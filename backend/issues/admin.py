from django.contrib import admin
from .models import Issue, IssueCategory

admin.site.register(Issue)
admin.site.register(IssueCategory)
