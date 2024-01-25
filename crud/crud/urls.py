from django.contrib import admin
from django.urls import path

from crudop.views import *

urlpatterns = [
    path('', StudentView.as_view()),
    path('form/', Studentadd.as_view(), name="harshit"),
    path('datatable/', datatable.as_view(), name="data_table"),
    path('update/<int:id>/', updateview.as_view(), name="update"),
    path('admin/', admin.site.urls),

]
