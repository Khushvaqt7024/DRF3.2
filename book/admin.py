from django.contrib import admin

from django_celery_beat.models import PeriodicTask,CrontabSchedule


# CrontabSchedule yaratish (Har kuni soat 9:00 da)

crontab_schedule, created = CrontabSchedule.objects.get_or_create(

    minute="0",  # Soatning 0-da, ya'ni har soatning boshida

    hour="9",  # Soat 9:00

    day_of_week="*",  # Har kuni

    day_of_month="*",  # Har oyda

    month_of_year="*",  # Har oydan

)


# PeriodicTask yaratish va crontabga ulash

# PeriodicTask.objects.create(
#
#     crontab=crontab_schedule,  # Yaratilgan crontab
#
#     name="Print Time Every Day at 9:00 AM",  # Task nomi
#
#     task="app.tasks.print_time",  # Celery task nomi
#
# )