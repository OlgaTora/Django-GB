from django.db import models
from django.utils import timezone


class HeadsOrTails(models.Model):
    result = models.CharField(max_length=100)
    result_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.result

    @staticmethod
    def result_stat(n: str):
        n = int(n)
        stat = {'heads': 0, 'tails': 0}
        query = list(HeadsOrTails.objects.all())
        results = query[-n:]
        for result in results:
            if 'heads' in str(result):
                stat['heads'] += 1
            elif 'tails' in str(result):
                stat['tails'] += 1
        return stat
