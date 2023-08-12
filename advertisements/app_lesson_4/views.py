from django.shortcuts import render
from django.http import HttpResponse



def lesson_4(request):
    html_content = '<html><head><title>Домашние задание</title></head><body>'
    html_content += '<h1>Домашка по 4 занятию</h1>'
    html_content += """<p>В рамках проекта с вебинара создайте еще одно приложение таким же образом, как мы делали на занятии и дайте ему название app_lesson_4.<br> Создайте в нем представление (view), которое будет возвращать ответ: «Домашка по 4 занятию». Подключите приложение к проекту. Сделайте, так, чтобы представление работало по следующему адресу: http://127.0.0.1/lesson_4.<br>
В качестве решения прикрепите ссылку на репозиторий git. <br> <br></p>"""

    html_content += '</body></html>'
    return HttpResponse(html_content)

# Create your views here.
#До встречи!Удачи!Всего наилучшего!Успехов!