from django_enhanced.urls import *

print("TOOLBAR URLS")

urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]