from django.shortcuts import redirect, render
from django.urls import reverse


from .forms import InserationForm

def insert_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    if request.method == "POST":
        insert_form = InserationForm(request.POST, request.FILES)
        if insert_form.is_valid():
            form = insert_form.save(commit=False)
            form.inserter = request.user
            form.save()
            return redirect('index')
    else:
        insert_form = InserationForm()
    context['insert_form'] = insert_form
    return render(request, 'inseration/insert.html', context)
