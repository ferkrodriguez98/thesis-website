from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_protect

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/success/'
    template_name = 'person_form.html'

def home(request):
    return render(request, 'home.html')

@csrf_protect  # Apply the CSRF protection to this view
def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            return redirect('app_tesis:success')
        else:
            errors = form.errors.as_data()
            form = PersonForm()
    else:
        form = PersonForm()
        errors = {}
    
    file = open('preguntas.txt', 'r')
    questions = file.readlines()
    file.close()
    
    questions_codes = ['ext1', 'ext2', 'ext3', 'ext4', 'ext5', 'ext6', 'ext7', 'ext8', 'ext9', 'ext10', 'est1', 'est2', 'est3', 'est4', 'est5', 'est6', 'est7', 'est8', 'est9', 'est10', 'agr1', 'agr2', 'agr3', 'agr4', 'agr5', 'agr6', 'agr7', 'agr8', 'agr9', 'agr10', 'csn1', 'csn2', 'csn3', 'csn4', 'csn5', 'csn6', 'csn7', 'csn8', 'csn9', 'csn10', 'opn1', 'opn2', 'opn3', 'opn4', 'opn5', 'opn6', 'opn7', 'opn8', 'opn9', 'opn10']
    
    questions_and_question_codes = zip(questions, questions_codes)

    return render(request, 'person_form.html', {'form': form, 'questions_and_questions_codes': questions_and_question_codes, 'errors' : errors})


def success(request):
    return render(request, 'success.html')