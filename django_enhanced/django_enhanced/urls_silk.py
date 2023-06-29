from django_enhanced.urls import *

print("SILK URLS")

urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]