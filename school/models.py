from django.db import models

# Create your models here.
class bookresult(models.Model):
    rollno = models.IntegerField(primary_key=True, default=0)
    regno = models.CharField(max_length=23, default='2021-UOK-04201')
    sname = models.CharField(max_length=39, default='')
    fname = models.CharField(max_length=50, default='')
    session = models.CharField(max_length=50, default='BS Software Engineering Fall (2021-2025)')
    semester = models.CharField(max_length=49, default='Spring 2023 4th Semester')

    courdecode = models.CharField(max_length=34, default='SE-3101')
    crhours = models.IntegerField(default=4)
    lettergrage = models.CharField(max_length=34, default='A')
    bname = models.CharField(max_length=199, default='Web Engineering')
    tmark = models.IntegerField(default=200)
    omark = models.IntegerField(default=145)
    percentage = models.FloatField(default=50.0)

    courdecode1 = models.CharField(max_length=34, default='SE-3106')
    crhours1 = models.IntegerField(default=4)
    lettergrage1 = models.CharField(max_length=34, default='A')
    bname1 = models.CharField(max_length=199, default='Professional Practices')
    tmark1 = models.IntegerField(default=200)
    omark1 = models.IntegerField(default=145)
    percentage1 = models.FloatField(default=50.0)

    courdecode2 = models.CharField(max_length=34, default='CS-3102')
    crhours2 = models.IntegerField(default=4)
    lettergrage2 = models.CharField(max_length=34, default='A')
    bname2 = models.CharField(max_length=199, default='Information Security')
    tmark2 = models.IntegerField(default=200)
    omark2 = models.IntegerField(default=145)
    percentage2 = models.FloatField(default=50.0)

    courdecode3 = models.CharField(max_length=34, default='SE-3104')
    crhours3 = models.IntegerField(default=4)
    lettergrage3 = models.CharField(max_length=34, default='A')
    bname3 = models.CharField(max_length=199, default='Software Quality Engineering')
    tmark3 = models.IntegerField(default=200)
    omark3 = models.IntegerField(default=145)
    percentage3 = models.FloatField(default=50.0)

    courdecode4 = models.CharField(max_length=34, default='EG-3103')
    crhours4 = models.IntegerField(default=4)
    lettergrage4 = models.CharField(max_length=34, default='A')
    bname4 = models.CharField(max_length=199, default='Machine Learning')
    tmark4 = models.IntegerField(default=200)
    omark4 = models.IntegerField(default=145)
    percentage4 = models.FloatField(default=50.0)

    courdecode5 = models.CharField(max_length=34, default='CS-3102')
    crhours5 = models.IntegerField(default=4)
    lettergrage5 = models.CharField(max_length=34, default='A')
    bname5 = models.CharField(max_length=199, default='Human Resource Management')
    tmark5 = models.IntegerField(default=200)
    omark5 = models.IntegerField(default=145)
    percentage5 = models.FloatField(default=50.0)

    # Repeat the same correction for courdecode2, courdecode3, courdecode4, and courdecode5

    gpa = models.FloatField(default=3.00)
    remarks = models.CharField(max_length=34, default='Promoted')

    def __str__(self):
        return self.sname
