from django.db import models


class Attendee(models.Model):
    register_id = models.CharField(max_length=7)
    register_name = models.CharField(max_length=50, default=' ')
    register_type = models.CharField(max_length=8)

    # 参加者マスタのテーブル名を指定
    class Meta:
        db_table = 'Attendee'

    def __str__(self):
        return self.register_id
