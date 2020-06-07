from pathlib import Path
import pandas as pd
import io
import csv
from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


# class Clustering(models.Model):
#     # csv_file = file = models.FileField()
#     latitude_name = models.TextField()
#     longitude_name = models.TextField()
#     # features_name_list = models.ExpressionList()

def import_file(path):
    suffix = Path(str(path)).suffix
    if suffix != '.csv':
        return
    # decoded_file = path.read().decode("iso-8859-1")
    # io_string = io.StringIO(decoded_file)
    # csv_reader = csv.DictReader(io_string, delimiter=';')
    # columns = cls.columns
    # errors = []
    return pd.read_csv(path)

