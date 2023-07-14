from graphene_django.views import GraphQLView
from django.urls import path
from .schema import schema


urlpatterns = [
    path('posts/',GraphQLView.as_view(graphiql = True,schema = schema))

]