from django.views.generic.base import TemplateView
from django.core.paginator import Paginator

import public.models as model

class IndexView(TemplateView):
    template_name='pages/index.html'

    def get(self, request, *args, **kwargs):

        iTour = model.Tours.objects.filter(online=True).order_by('id')
        iSettings = model.Settings.objects.filter(IsActive=True).first()

        context = super().get_context_data(**kwargs)
        context.update({
            'iTour':iTour,
            'iSettings':iSettings
        })
        return self.render_to_response(context)

class AboutView(TemplateView):
    template_name='pages/nuevo.html'

class ToursView(TemplateView):
    template_name='pages/tours.html'

    def get(self, request, *args, **kwargs):

        ITEMS = 4
        
        TourList = model.Tours.objects.filter(online=True).order_by('id')
        iTour = Paginator(TourList,ITEMS).get_page(request.GET.get('page')) if TourList else []
        
        iTourFix = range(0,(ITEMS - len(TourList)%ITEMS))
        
        if iTourFix == ITEMS and len(TourList) != 0:
            iTourFix = range(0,0)
        
        context = super().get_context_data(**kwargs)
        context.update({
            'iTour':iTour
        })
        return self.render_to_response(context)