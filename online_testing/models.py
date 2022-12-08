from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class SetQuestionnaire(models.Model):
    topic = models.CharField(max_length=50, verbose_name="Название/Тема теста")
    date_publication = models.DateField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.topic

    def __repr__(self):
        return f"<Tест: {self.topic}>"

    def get_absolute_url(self):
        return reverse("test", kwargs={"pk": self.pk})


class ListQuestion(models.Model):
    questionnaire = models.ForeignKey(
        SetQuestionnaire, on_delete=models.CASCADE, verbose_name="Название/Тема теста"
    )
    question = models.TextField(verbose_name="Вопрос")

    def __str__(self):
        return self.question


class OptionAnswer(models.Model):
    STATUS = [("True", "Верно"), ("False", "Неверно")]
    question = models.ForeignKey(ListQuestion, on_delete=models.CASCADE, verbose_name="Вопрос")
    option = models.TextField(choices=STATUS, verbose_name="Ответ")

    def __str__(self):
        return self.option


class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    questionnaire = models.ForeignKey(
        SetQuestionnaire, on_delete=models.CASCADE, verbose_name="Название/Тема теста"
    )
    right_answer = models.IntegerField(default=0, verbose_name="Верные ответы")
    wrong_answer = models.IntegerField(default=0, verbose_name="Неверные ответы")
    status = models.BooleanField(default=False, verbose_name="Пройдено/ не пройдено")
    date_pass = models.DateField(auto_now=True, verbose_name="Дата прохождения")

    def __str__(self):
        return f"{self.user}: {self.questionnaire}, {self.right_answer}"

    def __repr__(self):
        return (
            f"<Статистика: {self.user} прошел тест: {self.questionnaire} c результатами: "
            f"верные ответы - {self.right_answer} и неверные - {self.wrong_answer}> "
        )
