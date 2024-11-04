from django.urls import path
from .views import Get_Sin,Get_Cos,Get_Tan,Get_Cot
urlpatterns=[
    path('get_sin/<value>',Get_Sin.as_view(),name='get_sin'),
path('get_cos/<value>',Get_Cos.as_view(),name='get_cos'),
path('get_tan/<value>',Get_Tan.as_view(),name='get_tan'),
path('get_cot/<value>',Get_Cot.as_view(),name='get_cot')
]