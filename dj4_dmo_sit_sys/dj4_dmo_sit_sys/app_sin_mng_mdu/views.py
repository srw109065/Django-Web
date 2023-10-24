from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SigninLog
from datetime import datetime


# Create your views here.
def hello_world(request):
    dict_resp = {
        "current_time": str(datetime.now()),
    }

    return render(request, "hello_world.html", dict_resp)


def do_calculate(request):
    int_a = 10
    int_b = 20
    int_result = int_a + int_b
    print("int_result:", int_result)

    str_return = str(int_a) + " + " + str(int_b) + " = " + str(int_result)

    return HttpResponse(str_return)

#測試 更新 登入
def do_get_signin_log(request):
    dict_resp = {
        "current_time": str(datetime.now()),
    }

    qryset_signin_log = SigninLog.objects.all()
    print(qryset_signin_log)

    qryset_user = User.objects.filter(username="superuser")
    print(len(qryset_user))

    if len(qryset_user) == 1:
        SigninLog.objects.create(
            user_id=qryset_user[0],
            username=qryset_user[0].username,
            first_name=qryset_user[0].first_name,
            last_name=qryset_user[0].last_name,
        )

    qryset_signin_log = SigninLog.objects.order_by("-signin_datetime")
    print(qryset_signin_log)

    print("qryset_user[0].email:", qryset_user[0].email)
    qryset_user.update(email="123@gmail.com")
    print("qryset_user[0].email:", qryset_user[0].email)

    qryset_signin_log = SigninLog.objects.all()
    print(len(qryset_signin_log))
    qryset_signin_log.delete()
    print(len(qryset_signin_log))

    return render(request, "acc_sig_pge.html", dict_resp)


def go_signin_page(request):
    dict_resp = {
        "current_time": str(datetime.now()),
    }

    return render(request, "acc_sig_pge.html", dict_resp)


def do_signin(request):
    if request.method == "POST":
        str_username = request.POST.get("username")
        str_password = request.POST.get("password")

        obj_auth_user = authenticate(
            request,
            username=str_username,
            password=str_password
        )

        if obj_auth_user:
            login(
                request,
                obj_auth_user
            )

            request.session["from_redirect"] = True

            return redirect("go_ord_mng_page")

    return go_signin_page(request)


def do_logout(request):
    if request.method == "POST":
        logout(request)

    return redirect("go_signin_page")


@api_view(["POST"])
def api_get_user_list(request):
    dict_resp_rlt = {
        "status": "",
        "messages": "",
        "lst_user": "",
    }

    try:
        dict_api_data = request.data

        if dict_api_data["get_user"] == "Y":
            lst_username = []
            qryset_user = User.objects.all()

            for obj_user in qryset_user:
                lst_username.append(obj_user.username)

            dict_resp_rlt["lst_user"] = lst_username

        dict_resp_rlt["status"] = "SUCCESS"
    except Exception as e:
        dict_resp_rlt["status"] = "FAIL"
        dict_resp_rlt["messages"] = str(e)

    return Response(dict_resp_rlt)

