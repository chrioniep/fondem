from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView
from website.models import Event
from .forms import DashboardForm

# Create your views here.
class DashViewCreate(View):


    def get(self, request, *args, **kwargs):
        form = DashboardForm()
        context = {
            'form':form,
        }
        return render(self.request, 'createEvent.html', context)

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            form = DashboardForm(self.request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
            
                event = Event.objects.create(
                    title=title,
                    content=content
                )
                event.save()
            return redirect("website:news")
        


class DashViewHome(View):
     def get(self, request):
         events = Event.objects.all()
         context = {
             'events':events
         }
         return render(self.request, 'dashboard.html', context)

class DashViewUpdate(UpdateView):
    model = Event
    fields = ['title', 'content']
    template_name = "event_update.html"
    

def delete_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    a_event = Event.objects.get(slug=event.slug)
    a_event.delete()

    return redirect('dash:home')