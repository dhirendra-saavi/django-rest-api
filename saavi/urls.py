from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
 
from rest_api import rest_views, serializers


router = routers.DefaultRouter()
  
schema_view = get_schema_view(title='Saavi Rest API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
router.register(r'saavi-employee-test', rest_views.EmployeeTableList, 'saavi-employee-test') 

urlpatterns = [ 
     
    #Rest Api..
    path('', schema_view, name= 'v3.doc'),
    path('index/', rest_views.index, name= 'index'),
    path('api-', include(router.urls)),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
