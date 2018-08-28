from django.db import models

# Create your models here.
class HasTimestampModel(models.Model):
    created = models.DateTimeField('作成日時', auto_now_add=True)
    updated = models.DateField('更新日',help_text='メールアドレス')

    class Meta:
        abstract = True

class User(HasTimestampModel):
    id = models.AutoField(primary_key=True)
    emp_code = models.CharField('社員番号', max_length=10, help_text='社員番号')
    emp_name = models.CharField('社員名', max_length=150, help_text='社員名')
    email = models.CharField('メールアドレス', max_length=250, help_text='メールアドレス')

    class Meta:
        ordering = ('created',)

class WorkTime(HasTimestampModel):
    id = models.AutoField(primary_key=True)
    pj_name = models.CharField('業務名', max_length=250, help_text='業務名')
    reason = models.CharField('定時後作業不可避理由', max_length=250, help_text='定時後作業不可避理由')
    wk_reason = models.CharField('残業理由詳細', max_length=250, help_text='残業理由詳細')
    overtime = models.CharField('退社時間', max_length=100, help_text='退社時間')
    users = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)