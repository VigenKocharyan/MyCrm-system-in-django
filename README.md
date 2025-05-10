# 💼 MyCRM – Простая CRM-система на Django
# автор KocharyanVigen
MyCRM — это лёгкая в использовании CRM-система, разработанная на Django. Позволяет управлять клиентами и задачами через удобный веб-интерфейс.

![Главная страница](templates/screenshots/image.png)

## 🚀 Функции

- 📋 Список клиентов с фильтрацией и пагинацией
- ➕ Добавление, редактирование и удаление клиентов
- ✅ Аутентификация (Login/Logout)
- 📌 Задачи (tasks)
- 📱 Адаптивный интерфейс на Bootstrap 5

## 🛠 Установка

```bash
git clone https://github.com/твоя-ссылка/mycrm.git
cd mycrm
python -m venv env
source env/bin/activate  # или env\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
