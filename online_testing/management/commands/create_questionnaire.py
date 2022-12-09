from django.core.management.base import BaseCommand, CommandError

from online_testing.models import SetQuestionnaire, ListQuestion, OptionAnswer


class Command(BaseCommand):
    help = "Создание тестового опросника"

    def add_arguments(self, parser):
        parser.add_argument("creation", type=str)

    def handle(self, *args, **kwargs):
        creation = kwargs["creation"]
        if creation == "creation":
            self.create_questionnaire()
        else:
            self.stdout.write(self.style.UNSECCESS("Вы ввели неверную команду"))

    def create_questionnaire(self):
        questionnaire = SetQuestionnaire.objects.create(topic="Тестовый опросник")

        for questions in range(1, 5):
            self.create_question(questionnaire, questions)

    def create_question(self, questionnaire, questions):
        question = ListQuestion.objects.create(
            question=f"Вопрос №{questions}", questionnaire=questionnaire
        )
        self.create_answer(question)

    def create_answer(self, question):
        OptionAnswer.objects.bulk_create(
            [
                OptionAnswer(question=question, option="Неверно"),
                OptionAnswer(question=question, option="Верно"),
                OptionAnswer(question=question, option="Неверно"),
                OptionAnswer(question=question, option="Неверно"),
                OptionAnswer(question=question, option="Неверно"),
            ]
        )
