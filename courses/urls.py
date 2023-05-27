from django.urls import path
from .views import lesson, run, create_lesson, create_problem, add_problem

urlpatterns = [
    path("lesson/<int:pk>/", lesson, name="lesson"),
    path("run/<int:lesson>/<int:problem>/", run, name="run"),
    path("add_lesson/<str:username>/<str:password>/", create_lesson, name="add_lesson"),
    path("add_problem/<int:lesson>/<int:problem>/", add_problem, name="add_problem"),
    path("create_problem/<int:lesson>/", create_problem, name="create_problem")
]