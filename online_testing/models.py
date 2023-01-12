from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


CHOICES_STATUS = [
    ("1", "Да"),
    ("0", "Нет"),
]

CHOICES_OPTION_STATUS = [
    ("1", "Верно"),
    ("0", "Неверно"),
]


class Questionnaire(models.Model):
    topic_questionnaire = models.CharField(
        max_length=100,
        verbose_name="Тема тестового набора",
    )
    status_active = models.CharField(
        max_length=3,
        verbose_name="Статус",
        choices=CHOICES_STATUS,
        default=CHOICES_STATUS[0][0],
    )
    date_publication = models.DateField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        verbose_name = "Тестовый набор"
        verbose_name_plural = "Тестовые наборы"

    def __str__(self):
        return self.topic_questionnaire

    def get_absolute_url(self):
        return reverse("test", kwargs={"pk": self.pk})


class Question(models.Model):
    questionnaire_name = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        verbose_name="Тема тестового набора",
        blank=True,
        null=True,
    )
    question = models.CharField(
        max_length=250,
        verbose_name="Вопрос",
    )

    class Meta:
        ordering = ("questionnaire_name__id", "question")
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question


class OptionAnswer(models.Model):
    question_name = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Вопрос",
        blank=True,
        null=True,
    )
    option = models.CharField(
        max_length=10,
        choices=CHOICES_OPTION_STATUS,
        default=None,
        verbose_name="Вариант ответа",
    )

    class Meta:
        ordering = (
            "question_name__id",
            "option",
        )
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"

    def __str__(self):
        return self.option


class Statistic(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    questionnaire_name = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        verbose_name="Название тестового набора",
        blank=True,
        null=True,
    )
    right_answer = models.IntegerField(
        default=0,
        verbose_name="Верный ответ",
    )
    wrong_answer = models.IntegerField(
        default=0,
        verbose_name="Неверный ответ",
    )
    status_pass = models.BooleanField(
        default=False,
        verbose_name="Статус прохождения теста",
    )
    date_pass = models.DateField(
        auto_now=True,
        verbose_name="Дата прохождения теста",
    )

    class Meta:
        ordering = (
            "user",
            "questionnaire_name__id",
        )
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"

    def __str__(self):
        return f"{self.user}: {self.questionnaire_name}, {self.right_answer}, {self.wrong_answer}"

    def __repr__(self):
        return (
            f"<Статистика: {self.user} по тесту: {self.questionnaire_name} c результатами: "
            f"верные ответы - {self.right_answer}, неверные - {self.wrong_answer}> "
        )
