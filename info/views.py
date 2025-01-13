from django.shortcuts import get_object_or_404, render

from .models import Contact, News


def news_list(request):
    news_items = News.objects.order_by('-publication_date')
    return render(request, 'info/news_list.html', {'news_items': news_items})


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'info/news_detail.html', {'news_item': news_item})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'info/contact_list.html', {'contacts': contacts})
