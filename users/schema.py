import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from .models import User
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    all_users = graphene.List(UserNode)

    def resolve_all_users(self, info):
        return get_user_model().objects.all()
