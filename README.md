Финтрекер на Django

Описание проекта Финтрекер — веб-приложение для учета личных финансов: 
учет доходов и расходов - категории - бюджеты - отчеты

Архитектура:
users — пользователи 
categories — категории 
transactions —операции 
budgets — бюджеты 
reports — отчеты

Пошаговый план разработки:
1.  config/settings.py
    Подключить приложения
    Настроить БД
    Подключить DRF

2.  users/
    models.py — модель пользователя
    serializers.py — сериализация
    views.py — регистрация и авторизация 
    urls.py — маршруты

3.  categories/ 
    models.py — модель категории 
    serializers.py — сериализатор 
    views.py — CRUD 
    urls.py — маршруты

4.  transactions/
    models.py — модель транзакции
    serializers.py — cериализатор
    views.py — создание, список, фильтрация 
    urls.py — маршруты

5.  budgets/
    models.py — модель бюджета
    serializers.py — сериализатор
    views.py — установка и контроль
    urls.py — маршруты

6.  reports/
    views.py — отчеты
    urls.py — маршруты

7.  permissions.py
    Ограничение доступа

8.  Фильтрация transactions/views.py — фильтры

9.  tests.py
    тестирование

10. Финализация README.md — описание .gitignore — исключения

Запуск проекта: 
1. Виртуальное окружение 
2. Установка зависимостей
3. Миграции 
4. Суперпользователь 
5. Запуск сервера
