from pathlib import Path
import pandas as pd
import io
import csv

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


# class Clustering(models.Model):
#     # csv_file = file = models.FileField()
#     latitude_name = models.TextField()
#     longitude_name = models.TextField()
#     # features_name_list = models.ExpressionList()



class Algorithm(models.Model):
    df = None
    file = models.FileField(null=False)
    k = models.IntegerField(validators=[MinValueValidator(1)],
                            )
    eps = models.DecimalField(validators=[MinValueValidator(0)],
                              max_digits=5,
                              decimal_places=3,
                              )
    # algorithm = models.IntegerField(choices=((1, 'k_mxt'),
    #                                          (2, 'k_mxt')),
    #                                 default=1,
    #                                 )
