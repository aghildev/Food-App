from django.shortcuts import render,redirect
from django.http import HttpResponse
from foodapp.models import Item
from.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    item_list=Item.objects.all()
    my_dict={"item_list":item_list}
    return render(request,'foodapp/index.html',context=my_dict)

class indexClassView(ListView):
    model = Item;
    template_name="foodapp/index.html"
    context_object_name='item_list'

def details(request,item_id):
    item=Item.objects.get(pk=item_id)
    my_dict={"item":item}
    return render(request,'foodapp/details.html',context=my_dict)

class FoodDetail(DetailView):
    model = Item;
    template_name="foodapp/details.html"


def create_item(request):
    form=ItemForm(request.POST or None)


    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'foodapp/item-form.html',context={'form':form})
class CreateItem(CreateView):
    model=Item;
    fields=['Item_name', 'Item_desc','Item_price', 'Item_image']
    template_name="foodapp/item-form.html"

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('index')
    

    return render(request,'foodapp/item-form.html',context={'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('index')
    return render(request,'foodapp/item-delete.html',context={'item':item})
