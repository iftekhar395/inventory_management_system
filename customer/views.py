from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Customer


def customer_list(request, id=None):
  customers = Customer.objects.all()
  selected_customer = None
  if id:
    selected_customer = get_object_or_404(Customer, customer_id=id)

  context = {
    'customers': customers,
    'selected_customer': selected_customer
  }
  return render(request, 'customer.html', context)


def save_customer(request):
  if request.method == "POST":
    customer_id = request.POST.get('customer_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    address = request.POST.get('address')

    if customer_id:
      customer = get_object_or_404(Customer, customer_id=customer_id)
      customer.first_name = first_name
      customer.last_name = last_name
      customer.email = email
      customer.mobile = mobile
      customer.address = address
      customer.save()
    else:
      Customer.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        mobile=mobile,
        address=address
      )
    return redirect('customer')


def delete_customer(request, id):
  customer = get_object_or_404(Customer, customer_id=id)
  customer.delete()
  return redirect('customer')

# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
# from .models import Customer
#
# def customer(request,id=None):
#   customer_data = Customer.objects.all().values()
#   selected_customer = None
#   if id:
#     selected_customer = Customer.objects.get(customer_id=id)
#   cus_template = loader.get_template('customer.html')
#   context = {
#     'customers' : customer_data,
#     'selected_customer': selected_customer,
#   }
#   return HttpResponse(cus_template.render(context,request))
