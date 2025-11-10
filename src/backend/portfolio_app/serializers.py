from rest_framework import serializers
from .models import Hero, AboutMe, Skill, FuturePlan, Contact


class HeroSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)
    class Meta:
        model = Hero
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class FuturePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuturePlan
        fields = '__all__'
              
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'