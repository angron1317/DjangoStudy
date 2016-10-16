from django.db import models

from block.models import Block

# Create your models here.
class Article(models.Model):
    #block_id=models.IntegerField("板块ID")
    block=models.ForeignKey(Block,verbose_name="板块ID")
    title=models.CharField("板块名称",max_length=100)
    content=models.CharField("板块描述",max_length=10000)
    status=models.IntegerField("状态",choices=((0,"正常"),(-1,"删除")))

    #block_id=article.bolock_id
    #block=Block.objects.get(id=block_id)
    #block.name


    create_timestamp=models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp=models.DateTimeField("最后更新时间",auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="文章"
        verbose_name_plural="文章"











