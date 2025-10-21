from django.db import models


# === 1. HERO СЕКЦІЯ ===
class Hero(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім’я")
    profession = models.CharField(max_length=100, verbose_name="Професія / роль")
    introduction = models.TextField(verbose_name="Коротке привітання")
    photo = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.name


# === 2. ПРО СЕБЕ (ABOUT ME) ===
class AboutMe(models.Model):
    bio = models.TextField(verbose_name="Опис про себе")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата народження")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Місто проживання")

    def __str__(self):
        return "Про мене"


# === 3. ОСВІТА ===
class Education(models.Model):
    institution = models.CharField(max_length=100, verbose_name="Заклад освіти")
    degree = models.CharField(max_length=100, verbose_name="Спеціальність / ступінь")
    start_year = models.IntegerField(verbose_name="Рік початку навчання")
    end_year = models.IntegerField(verbose_name="Рік закінчення навчання")

    def __str__(self):
        return f"{self.degree} — {self.institution}"


# === 4. НАВИЧКИ ===
class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва навички")
    level = models.IntegerField(default=0, verbose_name="Рівень володіння (%)")

    def __str__(self):
        return f"{self.name} ({self.level}%)"


# === 5. МАЙБУТНІ ПЛАНИ ===
class FuturePlan(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва цілі")
    description = models.TextField(verbose_name="Опис плану")
    deadline = models.DateField(blank=True, null=True, verbose_name="Кінцевий термін")

    def __str__(self):
        return self.title


# === 6. КОНТАКТИ ===
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім’я")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Повідомлення")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Надіслано")

    def __str__(self):
        return f"{self.name} ({self.email})"
