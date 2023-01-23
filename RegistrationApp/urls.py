from django.urls import path
from RegistrationApp import views

urlpatterns=[
    path('index/',views.index,name='index'),

    path('add_admin/',views.add_admin,name='add_admin'),
    path('add_adminsave/',views.add_adminsave,name='add_adminsave'),
    path('fun_displayadmin/',views.fun_displayadmin,name='fun_displayadmin'),
    path('editadmin/<int:dataid>/',views.editadmin,name='editadmin'),
    path('updateadmin/<int:dataid>/',views.updateadmin,name='updateadmin'),
    path('deleteadmin/<int:dataid>/',views.deleteadmin,name='deleteadmin'),

    path('add_category/',views.add_category,name='add_category'),
    path('add_categorysave/',views.add_categorysave,name='add_categorysave'),
    path('fun_display/',views.fun_display,name='fun_display'),
    path('editcategory/<int:dataid>/', views.editcategory, name='editcategory'),
    path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
    path('deletecategory/<int:dataid>/',views.deletecategory,name='deletecategory'),


    path('add_book/',views.add_book,name='add_book'),
    path('add_booksave/',views.add_booksave,name='add_booksave'),
    path('fun_displaybook/',views.fun_displaybook,name='fun_displaybook'),
    path('editbook/<int:dataid>',views.editbook,name='editbook'),
    path('updatebook/<int:dataid>/',views.updatebook,name='updatebook'),
    path('deletebook/<int:dataid>/',views.deletebook,name='deletebook'),

    path('',views.adminloginpg,name='adminloginpg'),
    path('adminloginfun/',views.adminloginfun,name='adminloginfun'),

    path('emaildbfun/',views.emaildbfun,name='emaildbfun'),
    path('mssg/',views.mssg,name='mssg')


]