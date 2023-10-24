"""dj4_dmo_sit_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_sin_mng_mdu import views as app_sin_mng_mdu_views
from app_ord_mng_mdu import views as app_ord_mng_mdu_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("hello_world/", app_sin_mng_mdu_views.hello_world, name="hello_world"),
    path("do_calculate/", app_sin_mng_mdu_views.do_calculate, name="do_calculate"),
    path("do_get_signin_log/", app_sin_mng_mdu_views.do_get_signin_log, name="do_get_signin_log"),
    path("go_signin_page/", app_sin_mng_mdu_views.go_signin_page, name="go_signin_page"),
    path("do_signin/", app_sin_mng_mdu_views.do_signin, name="do_signin"),
    path("do_logout/", app_sin_mng_mdu_views.do_logout, name="do_logout"),
    path("api_get_user_list/", app_sin_mng_mdu_views.api_get_user_list, name="api_get_user_list"),

    path("go_ord_mng_page/", app_ord_mng_mdu_views.go_ord_mng_page, name="go_ord_mng_page"),
    path("do_show_order_detail/", app_ord_mng_mdu_views.do_show_order_detail, name="do_show_order_detail"),
    path("do_del_order/", app_ord_mng_mdu_views.do_del_order, name="do_del_order"),
    path("go_add_order_page/", app_ord_mng_mdu_views.go_add_order_page, name="go_add_order_page"),
    path("do_chk_order_and_item/", app_ord_mng_mdu_views.do_chk_order_and_item, name="do_chk_order_and_item"),
    path("do_save_order/", app_ord_mng_mdu_views.do_save_order, name="do_save_order"),
    path("api_get_order_info/", app_ord_mng_mdu_views.api_get_order_info, name="api_get_order_info"),
]
