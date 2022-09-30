from .models import Cate, Market
from django.views.generic import *
from django.shortcuts import render

# Create your views here.

class MarketLV(ListView):
    model = Market
    context_object_name = 'goods_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cate_list"] = Cate.objects.all()
        return context
    
    # template_name = 'market/market_list.html'
    # 
    # paginate_by = 6

def MarketCate(request, cate):
    queryset1 = Cate.objects.all()
    queryset2 = Market.objects.filter(cate = cate)

    context = {"cate_list": queryset1, "goods_list": queryset2}
    return render(request, "market/market_list.html", context)
    
class MarketDV(DetailView):
    model = Market

