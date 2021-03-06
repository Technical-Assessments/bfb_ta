from django.contrib import admin
from .models import Mentor, Project, Mentorship

from import_export.admin import ExportMixin, ImportExportMixin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget

admin.site.site_header = 'Mentor-Project Admin'

# Register your models here.

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'email']
    list_filter = ['gender']




""" class MentorResource(
    ExportMixin,
    admin.ModelAdmin
): """


class MentorResource(ExportMixin,
                    admin.ModelAdmin):
    
    projects = fields.Field(widget=ManyToManyWidget(Project))

    list_display = ['id', 'name', 'gender', 'email']

    class Meta:
        model = Mentor
        fields = ['id', 'name', 'gender', 'email', 'projects']



admin.site.register(Mentor, MentorAdmin)
admin.site.register(Project)
admin.site.register(Mentorship)
