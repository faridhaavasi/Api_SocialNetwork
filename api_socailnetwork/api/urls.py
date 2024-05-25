from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('api_socailnetwork.blog.urls', 'blog')))
    path('users/', include(('api_socialnetwork.User.urls', 'users'))),

]
