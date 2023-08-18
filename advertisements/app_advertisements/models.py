from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.html import format_html

User = get_user_model()


# Заголовок
# Описание
# Цена
# Дата
# Дата создания
# Дата обновления

# Create your models here.
class Advertisements(models.Model):
    title = models.CharField("заголовок",max_length=128)
    description = models.TextField("описание ")
    price = models.DecimalField("цена",max_digits=100,decimal_places=2)
    negotiable = models.BooleanField("торг",help_text="отметьте,если уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Отступ
    #Отступ
    user = models.ForeignKey(User,verbose_name="пользователь",on_delete=models.CASCADE)
    #Отступ
    image = models.ImageField("Изображение",upload_to="advertisements/")

    class Meta:
        db_table = "Advertisements"
        verbose_name = "Advertisements"
        verbose_name_plural = "Advertisements"


    def __str__(self):
        return f"Advertisements(id = {self.id},title = {self.title},price = {self.price},negotiable = {self.negotiable})"


    @admin.display(description="дата создания объявления")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color:green;font-weight:bold;'>Сегодня в {} </span>", created_time
        )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

   # @admin.display(description="обновлено")
    #def updated_date(self):
        #created_time = self.updated_at.time().strftime("%Y-%m-%d %H:%M:%S")
        #return format_html(
           # "<span style='color:green;font-weight:bold;'> {} </span>", created_time Как сделать,чтобы показывалась дата создания,даже если не сегодня
        #)

    @admin.display(description="дата обновления объявления")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color:#99f0b0;font-weight:bold;'>Сегодня в {} </span>", updated_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='изображение')
    def image_display(self):
        if self.image:
            return format_html(
                '<img src="{}" style="width: 55px;">', self.image.url
            )
        else:
            return 'No Image'


