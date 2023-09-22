from django.db import models
    
class Person(models.Model):
    birth_date = models.DateField()
    birth_hour = models.TimeField()
    birth_location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    happiness_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext6 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext7 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext8 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext9 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    ext10 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est6 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est7 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est8 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est9 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    est10 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr6 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr7 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr8 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr9 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    agr10 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn6 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn7 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn8 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn9 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    csn10 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn6 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn7 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn8 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn9 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    opn10 = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)