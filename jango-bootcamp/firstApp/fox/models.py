from django.db import models

# Create your models here.
class Entry:
    def __init__(self, head, desc):
        self.head = head
        self.desc = desc
