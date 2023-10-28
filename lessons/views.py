from django.shortcuts import render, redirect
from django.utils import timezone
from html_sanitizer import Sanitizer
from lessons.models import Subject, Lesson
from django.contrib.auth.decorators import login_required
import core.helpers.request_helpers as helpers
from lessons.forms.lesson_forms import AddSubject, CreateLesson
from core.helpers.site_constants import html_sanitizer_settings


@login_required(login_url="/login/")
def index(request):
    context = helpers.prepare_context(request)
    context['title'] = 'Blog'
    lessons = Lesson.objects.all()
    context['lessons'] = lessons
    return render(request, 'lessons/index.html', context=context)


@login_required(login_url="/login/")
def create_lesson(request):
    context = helpers.prepare_context(request)

    context['form'] = CreateLesson(None)

    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        tags = request.POST.get('tags').split(', ')
        author_id = helpers.get_user_id(request)

        subject_object = Subject.objects.filter(name=subject)
        if not subject_object:
            context['message'] = 'Please enter a subject.'
            return render(request, 'core/error.html', context=context)

        new_lesson = Lesson(
            title=title,
            subject=subject_object.first(),
            content=content,
            tags=tags,
            date_posted=timezone.now(),
            author_id=author_id
        )
        new_lesson.save()

        print(f"Lesson created: {title}")
        return redirect('index')

    return render(request, 'lessons/createlesson.html', context=context)


@login_required(login_url="/login/")
def view_lesson(request, lesson_id):
    context = helpers.prepare_context(request)

    lesson = Lesson.objects.filter(
        id=lesson_id).select_related('author').first()
    context['lesson'] = lesson

    # VALIDATE HTML
    sanitizer = Sanitizer(settings=html_sanitizer_settings)
    sanitized_html = sanitizer.sanitize(
        lesson.content).replace('{br}', chr(10))
    context['lesson_body'] = sanitized_html

    return render(request, 'lessons/viewlesson.html', context=context)


@login_required(login_url="/login/")
def edit_lesson(request, lesson_id):
    context = helpers.prepare_context(request)

    lesson = Lesson.objects.filter(
        id=lesson_id).select_related('author').first()

    if context['username'] != lesson.author.username:
        context['message'] = 'You are not the author of this lesson!'
        return render(request, 'core/accessdenied.html', context=context)

    context['lesson'] = lesson

    initial_form_data = {
        'title': lesson.title,
        'content': lesson.content,
        'subject': lesson.subject,
        'tags': ", ".join(lesson.tags)
    }

    context['form'] = CreateLesson(initial=initial_form_data)

    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        tags = request.POST.get('tags').split(', ')

        subject_object = Subject.objects.filter(name=subject)
        if not subject_object:
            context['message'] = 'Please enter a subject.'
            return render(request, 'core/error.html', context=context)

        lesson.title = title
        lesson.subject = subject_object.first()
        lesson.content = content
        lesson.tags = tags
        lesson.save()

        print(f"Lesson updated: {title}")

        return redirect(view_lesson, lesson_id=lesson_id)

    return render(request, 'lessons/editlesson.html', context=context)


@login_required(login_url="/login/")
def add_subject(request):
    context = helpers.prepare_context(request)
    if not context['admin']:
        return render(request, 'core/accessdenied.html', context=context)

    context['form'] = AddSubject(None)

    if request.method == 'POST':
        name = request.POST.get('name')

        new_subject = Subject(
            name=name.title(),
            date_created=timezone.now()
        )
        new_subject.save()

        print(f"Subject created: {name.title()}")

    return render(request, 'lessons/addsubject.html', context=context)
