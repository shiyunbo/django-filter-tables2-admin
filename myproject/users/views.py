from django.shortcuts import render

# Core Django modules
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User

# Mixins from django filter2 and django_tables2
from django_tables2 import SingleTableView, RequestConfig
from django_filters.views import FilterView

# Which fields will be be used to filter users, similar to list_filter
from .filters import UserFilter

# Which fields will be be used to display users in tables, similar to list_display
from .tables import UserTable

# Which fields will be used to add and update users
from .forms import UserForm


# Manage Users
class UserAdminTableView(LoginRequiredMixin, SingleTableView, FilterView):
    filter = None
    filter_class = UserFilter
    table_class = UserTable
    template_name = 'users/user_admin.html'


    def get_queryset(self, **kwargs):
        qs = User.objects.all().order_by('-id')
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = self.table_class(data=self.get_queryset())
        RequestConfig(self.request, paginate={"per_page": 5}).configure(t)
        context['filter'] = self.filter
        context['table'] = t
        return context


# create
class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'users/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('users:user_admin')

# update
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/user_form.html'
    form_class =  UserForm
    success_url = reverse_lazy('users:user_admin')

# Delete
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_admin')
