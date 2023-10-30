from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createlesson/", views.create_lesson, name="create_lesson"),
    path("viewlesson/<lesson_id>/", views.view_lesson, name="view_lesson"),
    path("editlesson/<lesson_id>/", views.edit_lesson, name="edit_lesson"),
    path("addcomment/<lesson_id>/", views.add_comment, name="add_comment"),
    path("editcomment/<comment_id>/", views.edit_comment, name="edit_comment"),
    path("deletecomment/<comment_id>/",
         views.delete_comment, name="delete_comment"),
    path("addsubject/", views.add_subject, name="add_subject")
]
