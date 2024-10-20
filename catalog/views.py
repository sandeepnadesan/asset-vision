from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Count, Q
from .models import Device, Customer, Model, Tracker, Inventory
from django.views import generic
from django.urls import reverse

# Create your views here.
def index(request):
    """
    Index page with count stock
    """
    # Count all devices
    num_devices = Device.objects.all().count()

    # Count devices by hostname type
    num_laptops = Device.objects.filter(hostname__icontains='laptop').count()  # Laptops
    num_desktops = Device.objects.filter(hostname__icontains='desktop').count()  # Desktops
    num_monitors = Device.objects.filter(hostname__icontains='monitor').count()  # Monitors

    num_dl_dep = Device.objects.filter(status__exact='1').count()  # Deployed devices
    num_dv_new = Device.objects.filter(status__exact='0').count()  # New devices
    num_dv_stk = Device.objects.filter(status__exact='3').count()  # Stock devices

    num_authors = Customer.objects.count()

    # Store visit count
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the template with context
    return render(
        request,
        'index1.html',
        context={
            'num_devices': num_devices,
            'num_authors': num_authors,
            'num_visits': num_visits,
            'num_laptops': num_laptops,
            'num_desktops': num_desktops,
            'num_monitors': num_monitors,
            'num_dl_dep': num_dl_dep,
            'num_dv_stk': num_dv_stk,
            'num_dv_new': num_dv_new,
        },
    )
    reverse('catalog_index1', args=())

""" Device List view """
class DeviceListView(generic.ListView):
    model = Device
    context_object_name = 'device_list'   # Custom context variable name in template
    list_display = ('title', 'display_model', 'customer', 'display_status', 'serialn', 'substatus', 'tag')
    queryset = Device.objects.all()
    template_name = 'catalog/device_list.html'

    def get_queryset(self):
        return Device.objects.all()

""" Device detail view """
class DeviceDetailView(generic.DetailView):
    model = Device

    def device_detail_view(request, pk):
        try:
            device_id = Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404("Device does not exist")

        return render(
            request,
            'catalog/device_detail.html',
            context={'device': device_id}
        )

""" Customer list view """
class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'   # Custom context variable name in template
    list_display = ('last_name', 'first_name', 'department', 'location')
    queryset = Customer.objects.all()
    template_name = 'catalog/customer_list.html'
    paginate_by = 30

    def get_queryset(self):
        return Customer.objects.all()

""" Customer detail view """
class CustomerDetailView(generic.DetailView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'catalog/customer_detail.html'

    def get_queryset(self):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        cid = get_object_or_404(Customer, pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['customer_detail'] = Device.objects.filter(customer_id=cid)
        return context

""" Tracker list view """
class TrackerListView(generic.ListView):
    model = Tracker
    context_object_name = 'tracker_list'
    template_name = 'catalog/tracker_list.html'
    paginate_by = 30

""" Tracker detail view """
class TrackerDetailView(generic.DetailView):
    model = Tracker
    context_object_name = 'tracker'
    template_name = 'catalog/tracker_detail.html'

    def get_queryset(self):
        return Tracker.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracker_listkz'] = Customer.objects.all()
        return context

""" Search view """
class SearchResultsView(generic.ListView):
    model = Device
    template_name = 'search_result.html'

    def get_queryset(self):  # New
        query = self.request.GET.get('q')
        object_list = Device.objects.filter(
            Q(title__icontains=query) | 
            Q(status__icontains=query) |
            Q(serialn__icontains=query) | 
            Q(customer__last_name__icontains=query) | 
            Q(model__name__icontains=query)
        )
        return object_list

""" Inventory data view """
class InventoryListView(generic.ListView):
    model = Inventory
    context_object_name = 'object_list'
    template_name = 'inv.html'
    paginate_by = 48
