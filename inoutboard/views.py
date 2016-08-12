from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from inoutboard.models import Staff
from inoutboard.forms import StaffForm, ContactForm
from django.shortcuts import render_to_response


def message_board(request):
    if 'message' in request.POST and request.POST['message']:#error prevention
        s = Staff.objects.get(pk=request.POST['staff_id'])
        s.message = request.POST['message']
        s.save()
    if 'out' in request.POST and request.POST['out']:
        c = Staff.objects.get(pk=request.POST['staff_id'])
        c.status = False
        c.save()
    if 'in' in request.POST and request.POST['in']:
        c = Staff.objects.get(pk=request.POST['staff_id'])
        c.status = True
        c.save()
    else:
        message = 'no changes to submit.'
    return render(request,'message_board.html', {'staff': Staff.objects.all().order_by('name'),})

# def contact(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = StaffForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             s = Staff.objects.get(pk=request.POST['staff_id'])
#             s.message = request.POST['message']
#             s.save()
#     else:
#         form = StaffForm() # An unbound form
#
#     return render_to_response('contact.html', {
#         'form': form,
#         'staff': Staff.objects.all().order_by('name'),
#     })
