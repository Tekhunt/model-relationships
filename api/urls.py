from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path
from .views import LoginView, delete_item, getData,\
    postData, itemDetails, update_item
from django.urls import path

from .views import PollList, ChoiceList, CreateVote, UserCreate
from rest_framework.authtoken import views

from rest_framework_swagger.views import get_swagger_view

from rest_framework.documentation import include_docs_urls


schema_view = get_swagger_view(title='2023 Polls API')


urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    # path("login/", views.obtain_auth_token, name="login"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path('', getData),
    path('add-item/', postData),
    path('details/<str:pk>/', itemDetails),
    path('update/<str:pk>/', update_item),
    path('delete/<str:pk>/', delete_item),
    path(r'swagger-docs/', schema_view),
    # path('openapi', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …"
    # ), name='openapi-schema'),
    path(r'docs/', include_docs_urls(title='Polls API')),

]
