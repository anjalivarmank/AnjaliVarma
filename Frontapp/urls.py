from django.urls import path
from Frontapp import views

urlpatterns=[
    path('',views.homepg,name='homepg'),
    path('aboutpg/',views.aboutpg,name='aboutpg'),
    path('blogpg/',views.blogpg,name='blogpg'),
    path('contactpg/',views.contactpg,name='contactpg'),
    path('productpg/',views.productpg,name='productpg'),
    path('discat/<itemcatg>/',views.discat,name='discat'),
    path('detailpg/<int:dataid>',views.detailpg,name='detailpg'),
    path('loginpg/',views.loginpg,name='loginpg'),
    path('signuppg/',views.signuppg,name='signuppg'),
    path('signupfun/',views.signupfun,name='signupfun'),
    path('loginfun/',views.loginfun,name='loginfun'),
    path('logoutfn/',views.logoutfn,name='logoutfn'),
    path('mssgfun/',views.mssgfun,name='mssgfun'),
    path('cartpg/',views.cartpg,name='cartpg'),
    path('cartdbfun/',views.cartdbfun,name='cartdbfun'),
    path('deleteitem/<int:dataid>',views.deleteitem,name='deleteitem')


]