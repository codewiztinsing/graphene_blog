from graphene_django import DjangoObjectType,DjangoListField
import graphene
from .models import Post
from django.contrib.auth.models import User



class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('first_name','last_name',"email","is_staff")

class PostObjectType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('name','author','date_created','date_updated')


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostObjectType)
    # all_users = DjangoListField(UserObjectType)
    # user = graphene.Field(UserObjectType,id = graphene.Int(),first_name = graphene.String(),last_name = graphene.String())

    def resolve_all_posts(root,context):
        print(context)
        return Post.objects.all()

    def resolve_user(root,info,id,first_name,last_name):
        print(id,first_name,last_name)
        return User.objects.get(id = id)

    # def resolve_all_users(root,context):
    #     return User.objects.all()

class PostMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)

    post = graphene.Field(PostObjectType)


    @classmethod

    def mutate(cls,root,info,name):
        post = Post(name = name)
        post.save()
        return PostMutation(post = post)


class Mutation(graphene.ObjectType):
    addPost = PostMutation.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)