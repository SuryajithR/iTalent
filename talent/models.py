from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    role = models.CharField(max_length=50, default='')
    status = models.IntegerField(default='1')

    def __str__(self):
        return "%s ,%s ,%s" % (self.name, self.email, self.password)


class talent_uploads(models.Model):
    can_id = models.ForeignKey(signup, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=501)
    files = models.ImageField(upload_to='skills', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return "%s" % (self.can_id.name)


class comment(models.Model):
    user_id = models.ForeignKey(signup, on_delete=models.CASCADE)
    talent_id = models.ForeignKey(talent_uploads, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()


class rating(models.Model):
    user_id = models.ForeignKey(signup, on_delete=models.CASCADE)
    talent_id = models.ForeignKey(talent_uploads, on_delete=models.CASCADE)
    rating = models.CharField(max_length=501, default='')


class gallery(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='skills')
