from django.urls import path
from .views import HeroList, AboutMeList, SkillList, FuturePlanList, ContactList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('heroes/', HeroList.as_view(), name='hero-list'),
    path('aboutme/', AboutMeList.as_view(), name='aboutme-list'),
    path('skills/', SkillList.as_view(), name='skill-list'),
    path('futureplans/', FuturePlanList.as_view(), name='futureplan-list'),
    path('contacts/', ContactList.as_view(), name='contact-list'),
]

