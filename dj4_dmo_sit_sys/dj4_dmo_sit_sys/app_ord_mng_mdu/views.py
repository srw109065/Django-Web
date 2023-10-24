from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Item
from app_sin_mng_mdu.views import go_signin_page
import json


def do_chk_string_is_float(string):
    try:
        float(string)

        return True
    except ValueError:
        return False


def do_chk_string_is_int(string):
    try:
        int(string)

        return True
    except ValueError:
        return False


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def go_ord_mng_page(request):
    dict_resp = {
        "qryset_order": Order.objects.all(),
    }

    if "from_redirect" in request.session:
        bol_from_redirect = request.session["from_redirect"]
        del request.session["from_redirect"]

        if bol_from_redirect:
            return render(request, "ord_mng_pge.html", dict_resp)

    return go_signin_page(request)


@login_required(login_url=settings.LOGIN_URL)
def do_show_order_detail(request):
    if request.method == "POST":
        dict_resp = {
            "item_content": "",
        }

        str_order_id = request.POST.get("orderId")
        print(str_order_id)
        qryset_item = Item.objects.filter(order=str_order_id)
        str_item_content = ""

        for obj_item in qryset_item:
            str_item_content += "<tr>"
            str_item_content += "<td>"
            str_item_content += obj_item.item_name
            str_item_content += "</td>"
            str_item_content += "<td>"
            str_item_content += str(obj_item.purchase_number)
            str_item_content += "</td>"
            str_item_content += "</tr>"

        dict_resp["item_content"] = str_item_content

        return HttpResponse(json.dumps(dict_resp), content_type="application/json")

    return go_signin_page(request)


@login_required(login_url=settings.LOGIN_URL)
def do_del_order(request):
    if request.method == "POST":
        dict_resp = {
            "qryset_order": "",
        }

        str_order_id = request.POST.get("orderId")
        qryset_order = Order.objects.filter(id=str_order_id)
        qryset_order.delete()

        dict_resp["qryset_order"] = Order.objects.all()

        return render(request, "ord_mng_pge.html", dict_resp)

    return go_signin_page(request)


@login_required(login_url=settings.LOGIN_URL)
def go_add_order_page(request):
    if request.method == "POST":
        return render(request, "ord_add_pge.html")

    return go_signin_page(request)


@login_required(login_url=settings.LOGIN_URL)
def do_chk_order_and_item(request):
    if request.method == "POST":
        dict_resp = {
            "check_result": "N",
        }

        str_ord_num = request.POST.get("ordNum")
        str_username = request.POST.get("username")
        str_tol_exps = request.POST.get("tolExps")
        lst_item_num = request.POST.getlist("itemNum")

        qryset_user = User.objects.filter(username=str_username)
        qryset_order = Order.objects.filter(username=str_username, order_num=str_ord_num)

        if len(qryset_user) == 1 and len(qryset_order) == 0 and do_chk_string_is_float(string=str_tol_exps):
            for i in range(len(lst_item_num)):
                if do_chk_string_is_int(string=lst_item_num[i]):
                    dict_resp["check_result"] = "Y"
                else:
                    dict_resp["check_result"] = "N"
                    break

        return HttpResponse(json.dumps(dict_resp), content_type="application/json")

    return go_signin_page(request)


@login_required(login_url=settings.LOGIN_URL)
def do_save_order(request):
    if request.method == "POST":
        dict_resp = {
            "qryset_order": "",
        }

        str_ord_num = request.POST.get("ordNum")
        str_username = request.POST.get("username")
        str_tol_exps = request.POST.get("tolExps")

        lst_item_nm = request.POST.getlist("itemNm")
        lst_item_num = request.POST.getlist("itemNum")

        qryset_user = User.objects.filter(username=str_username)

        if len(qryset_user) == 1:
            obj_user = qryset_user[0]

            obj_order = Order.objects.create(
                username=str_username,
                first_name=obj_user.first_name,
                last_name=obj_user.last_name,
                order_num=str_ord_num,
                total_expenses=float(str_tol_exps),
            )

            for i in range(len(lst_item_nm)):
                Item.objects.create(
                    order=obj_order,
                    item_name=lst_item_nm[i],
                    purchase_number=lst_item_num[i]
                )

            dict_resp["qryset_order"] = Order.objects.all()

            return render(request, "ord_mng_pge.html", dict_resp)

    return go_signin_page(request)


@api_view(["POST"])
def api_get_order_info(request):
    dict_resp_rlt = {
        "status": "",
        "messages": "",
        "dict_order": {},
        "lst_items": []
    }

    try:
        dict_api_data = request.data
        str_username = dict_api_data["str_username"]
        str_order_num = dict_api_data["order_num"]

        qryset_order = Order.objects.filter(username=str_username, order_num=str_order_num)

        if len(qryset_order) > 0:
            obj_order = qryset_order[0]
            qryset_item = Item.objects.filter(order_id=obj_order.id)

            dict_resp_rlt["dict_order"] = {
                "username": obj_order.username,
                "first_name": obj_order.first_name,
                "last_name": obj_order.last_name,
                "order_num": obj_order.order_num,
                "total_expenses": obj_order.total_expenses,
                "purchase_datetime": obj_order.purchase_datetime,
            }

            for obj_item in qryset_item:
                dict_resp_rlt["lst_items"].append(
                    {"item_name": obj_item.item_name, "purchase_number": obj_item.purchase_number}
                )

        dict_resp_rlt["status"] = "SUCCESS"
    except Exception as e:
        dict_resp_rlt["status"] = "FAIL"
        dict_resp_rlt["messages"] = str(e)

    return Response(dict_resp_rlt)
