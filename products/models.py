from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()

    #Ця функці треба для перенесення даних в базу данних і створення
    # таблиці з заголовками імя і ціна а ше це вноситься в адмінку
    def __str__(self):
        return self.name