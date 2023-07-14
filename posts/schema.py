from graphene_django import DjangoObjectType
import graphene
from .models import Post


class PostObjectType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('name','date_created','date_updated')


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostObjectType)

    def resolve_all_posts(root,context):
        print(context)
        return Post.objects.all()


schema = graphene.Schema(query=Query)