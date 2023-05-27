from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Lesson, Problem
import requests

@csrf_exempt
def lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    problems = {}
    for problem in lesson.problems.all():
        problems[problem.name] = {
                "id": problem.id,
                "timelimit": problem.timelimit,
                "memorylimit": problem.memorylimit,
                "difficulty": problem.difficulty,
                "problem": problem.problem,
                "comment": problem.comment,
                "infoin": problem.infoin,
                "infoout": problem.infoout,
                "simpletests": problem.simpletests
            }
    return JsonResponse(
        {
            "name": lesson.name,
            "id": lesson.id,
            "video": lesson.video,
            "body": lesson.body,
            "problems": problems,
            "created_at": lesson.created_at,
            "updated_at": lesson.updated_at,
            "viewers": lesson.viewers.count(),
        }
    )

token = "7f3b28a781ba850296fbd5ec5578f1787aa9e772"
url = "https://algorithmshubtestapi.pythonanywhere.com/test/"

@csrf_exempt
def run(request, lesson, problem):
    if request.method == "POST":
        try:
            lesson = Lesson.objects.get(id=lesson)
            problem = Problem.objects.get(id=problem)
            print(problem.tests)
            data = {
                "name": request.user.username,
                "code": request.POST.get("code"),
                "language": request.POST.get("language"),
                "userinput": request.POST.get("userinput"),
                "tests": str(problem.tests),
                "timelimit": problem.timelimit,
            }
            response = requests.post(
                url=url, 
                data=data,
                headers={
                    "Authorization": f"Token {token}"
                }
            )
            user = User.objects.get(id=request.POST.get("userid"))
            if response.json()["status"] == "Accepted":
                problem.solvers.add(user)
            return JsonResponse({
                "status": response.json()["status"],
                "time": response.json()["time"],
                "error": response.json()['error'],
            })
        except Exception as e:
            print(e)
    return JsonResponse(
        {
            "status": "failed"
        }
    )

@csrf_exempt
def create_lesson(request, username, password):
    if request.method == "POST":
        user = authenticate(request, username=username, password=password)
        if user.is_superuser:
            name = request.POST.get("name")
            body = request.POST.get("body")
            video = request.POST.get("video")
            Lesson.objects.create(
                name=name,
                body=body,
                video=video,
            )
            return JsonResponse({
                "status": "ok",
                "info": "Lesson created successfully"
            })
    return JsonResponse({
        "status": "failed"
    })

@csrf_exempt
def add_problem(request, lesson, problem):
    try:
        lesson = Lesson.objects.get(id=lesson)
        problem = Problem.objects.get(id=problem)
        lesson.problems.add(problem)
        return JsonResponse({
            "status": "ok",
            "info": "Problem added successfully"
        })
    except:
        return JsonResponse({
            "status": "failed"
        })

@csrf_exempt 
def create_problem(request, lesson):
    if request.method == "POST":
        lesson = Lesson.objects.get(id=lesson)
        name = request.POST.get("name")
        problem = request.POST.get("problem")
        comment = request.POST.get("comment")
        infoin = request.POST.get("infoin")
        infoout = request.POST.get("infoout")
        simpletests = request.POST.get("simpletests")
        tests = request.POST.get("tests")
        problem = Problem(
            name=name,
            problem=problem,
            comment=comment,
            infoin=infoin,
            infoout=infoout,
            simpletests=simpletests,
            tests=tests,
        )
        problem.save()
        lesson.problems.add(problem)
        return JsonResponse({
            "status": "ok",
            "info": "Problem created successfully"
        })
    return JsonResponse({
        "status": "failed"
    })