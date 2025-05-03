from django.db import migrations

CATEGORY_CHOICES = [
    ('user', 'User'),
    ('student', 'Student'),
    ('graduate', 'Graduate'),
    ('phd', 'PhD'),
    ('assistant_professor', 'Assistant Professor'),
    ('associate_professor', 'Associate Professor'),
    ('professor', 'Professor'),
    ('emeritus_professor', 'Emeritus Professor'),
    ('researcher', 'Researcher'),
    ('lecturer', 'Lecturer'),
]

def add_statuses(apps, schema_editor):
    Status = apps.get_model('status', 'Status')
    for code, name in CATEGORY_CHOICES:
        Status.objects.create(status_name=code)

def remove_statuses(apps, schema_editor):
    Status = apps.get_model('status', 'Status')
    Status.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_alter_status_options_alter_status_status_name'),
    ]

    operations = [
        migrations.RunPython(add_statuses, remove_statuses),
    ]