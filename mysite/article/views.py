from django.shortcuts import render
from django.views.generic import View

from block.models import Block
from .models import Article

def article_list(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,'article_list.html',{"articles":articles_objs,"b":block})
#block=block 也可以写filter(block__id=block_id)...两个下划线

#filter(block=block,status=0)...中逗号，表明与逻辑，等同and。
#如果你想表达或，需要使用Q对象，一个Q对象是一个限制条件。
#from django.db.models import Q
#filter(Q(block=block)|Q(status=0)&Q(x=y)




class ArticleCreateView(View):

    template_name = "article_create.html"

    def init_data(self, block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)

    def get(self, request, block_id):
        self.init_data(block_id)
        return render(request, self.template_name, {"b": self.block})

    def post(self, request, block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.block = self.block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % self.block_id)
        else:
            return render(request, self.template_name, {"b": self.block, "form": form})
