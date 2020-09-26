from django.db import models
from django.utils import timezone


class RushBook(models.Model):
    name = models.CharField(max_length=500)

    def total_rush(self):
        # total = self.rushlistmodel_set.all().aggregate(models.Sum('money'))
        # return total['money__sum']
        total = 0
        for item in self.rushlistmodel_set.all():
            if item.type:
                total += item.money
            else:
                total -= item.money
        return total

    def add_list(self, amount, lst_name, boolean):
        RushListModel.objects.create(book=self, money=amount, list_name=lst_name, post_date=timezone.now(), type=boolean)


class RushListModel(models.Model):
    book = models.ForeignKey(RushBook, on_delete=models.CASCADE)
    list_name = models.TextField()
    money = models.IntegerField()
    post_date = models.DateTimeField('post date')
    type = models.BooleanField()
