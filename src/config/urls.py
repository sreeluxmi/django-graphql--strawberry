from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from strawberry.django.views import GraphQLView, AsyncGraphQLView
from book.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=schema)),
    path('graphql/', AsyncGraphQLView.as_view(
            schema=schema,
            graphiql=settings.DEBUG,
            subscriptions_enabled=True,
        ),
    ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
