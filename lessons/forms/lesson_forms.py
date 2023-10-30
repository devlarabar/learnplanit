from django import forms
from ckeditor.widgets import CKEditorWidget
from lessons.models import Subject, Lesson

subjects_objects = Subject.objects.all().order_by('-name')
subjects_list = sorted([(s.name, s.name) for s in subjects_objects])


class AddSubject(forms.Form):
    name = forms.CharField(
        label='Name',
        min_length=3,
        max_length=200,
        required=True
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        name_exists = Subject.objects.filter(name__iexact=name)
        if name_exists.count():
            raise forms.ValidationError("Subject already exists.")
        return name


class CreateLesson(forms.Form):
    subjects = subjects_list
    title = forms.CharField(
        label='Title',
        min_length=3,
        max_length=100,
        required=True
    )
    content = forms.CharField(
        label='Content',
        required=True,
        widget=CKEditorWidget(),
    )
    tags = forms.CharField(
        label='Tags (comma-separated)',
    )
    subject = forms.ChoiceField(
        choices=subjects,
        required=True
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        title_exists = Lesson.objects.filter(title__iexact=title)
        if title_exists.count():
            raise forms.ValidationError("Title already exists.")
        return title


class AddComment(forms.Form):
    comment = forms.CharField(
        label='Comment',
        required=True,
        widget=CKEditorWidget(),
    )
