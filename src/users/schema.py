import strawberry
from strawberry.django import auth
from .types import User, UserInput


@strawberry.type
class Query:
    me: User = auth.current_user()


@strawberry.type
class Mutation:
    login: User = auth.login()
    logout = auth.logout()
    register: User = auth.register(UserInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)
