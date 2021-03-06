from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a specified product to the users shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = 1

    request.session['bag'] = bag
    messages.success(request, f'Added: {product.name}')

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ remove a specified product to the users shopping bag """
    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed: {product.name}')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Error when attempting to remove: {product.name}')
        return HttpResponse(status=500)
