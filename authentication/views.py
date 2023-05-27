from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            return JsonResponse(
                {"status": "ok"}
            )
    return JsonResponse({
        "status": "failed"
    })

@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        User.objects.create_user(username=username, password=password)
        return JsonResponse(
            {
                "status": "ok"
            }
        )        
    return JsonResponse(
        {"status": "failed"}
    )

@csrf_exempt
def profile(request, username):
    try:
        user = User.objects.all().filter(username=username).first()
        u_name = user.username
        f_name = user.first_name
        l_name = user.last_name
        return JsonResponse(
            {
                "status": "ok",
                "username": u_name,
                "first_name": f_name,
                "last_name": l_name,
            }
        )
    except:
        return JsonResponse(
            {
                "status": "failed"
            }
        )

@csrf_exempt
def users(request):
    d = {}
    for user in User.objects.all():
        d[f"{user.username}"] = {
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    return JsonResponse(
        d
    )