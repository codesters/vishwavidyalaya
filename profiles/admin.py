from django.contrib import admin
from profiles.models import Faculty, Student

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('empID', 'user', 'sex')
    list_editable = ['sex']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrolment_number', 'name', 'course')
    search_fields = ['name', 'email', 'form_number', 'enrolment_number']

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)