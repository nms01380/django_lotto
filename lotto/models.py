from django.db import models
from django.utils import timezone
import random
# Create your models here.

class GuessNumbers(models.Model):

    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')
    num_lottos = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1, 46)) # 1~45까지의 숫자들이 들어있는 리스트

        for _ in range(0, self.num_lottos): # range(0, 5) -> 0, 1, 2, 3, 4
            random.shuffle(origin) # 1~45 랜덤으로 섞기
            guess = origin[:6] # 섞인 상태에서 앞에 6개 추출
            guess.sort()

            self.lottos += str(guess) + '\n'

        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
