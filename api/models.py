from django.db import models

# Create your models here.
class HasTimestampModel(models.Model):
    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(HasTimestampModel):
    emp_code = models.CharField('社員番号', max_length=10, help_text='社員番号')
    emp_name = models.CharField('社員名', max_length=150, help_text='社員名')
    email = models.CharField('メールアドレス', max_length=250, help_text='メールアドレス')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        # db_table = "user"