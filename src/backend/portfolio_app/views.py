from rest_framework import generics
from .models import Hero, AboutMe, Skill, FuturePlan, Contact
from .serializers import HeroSerializer, AboutMeSerializer, SkillSerializer, FuturePlanSerializer, ContactSerializer

class HeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class AboutMeList(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class FuturePlanList(generics.ListAPIView):
    queryset = FuturePlan.objects.all()
    serializer_class = FuturePlanSerializer

class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
