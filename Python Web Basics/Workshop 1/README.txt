WORKSHOP 1 GUIDE

1.	Ctr + Alt + R, отваряме manage.py конзолата (или горе от менюто Tools) и пишем в конзолата startapp и името на папката (напр. common), която искаме да създадем. 
2.	Преместваме новосъздадената папка в главната директория на апликацията. 
3.	Добавяме новата папка common в главния settings.py, за да го открива.
4.	В common > views.py създаваме функция за вю landing_page.
5.	Създаваме нов файл urls.py в common. Вътре в него пишем urlpatterns = []. 
6.	В главния urls.py добавяме път към path(“”,  include(“petstagram.common.urls”)) , като добавяме django.urls import include като импорт. 
7.	Добавяме сваления от сайта темплейт landing_page.html в директорията templates ръчно.
8.	Закачаме новия темплейт в common > views.py чрез кодa return render(request, 'landing_page.html')
9.	В common > urls.py добавяме следния код from django.urls import path. След това добавяме връзка към нашия landing page - path('', landing_page) и за да сработи и да го намери, импортваме from petstagram.common.views import landing_page
10.	Отваряме пак manage.py конзолата и пишем migrate. 
