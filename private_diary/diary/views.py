from django.views import generic
from django.urls import reverse_lazy


from .forms import InquiryForm


import logging
logging = logging.getLogger(__name__)


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('diary:index')


    def form_valid(self, form):
        form.send_mail()
        logging.info(f'Inquiry sent by {form.cleaned_data['name']}')
        return super().form_valid(form)