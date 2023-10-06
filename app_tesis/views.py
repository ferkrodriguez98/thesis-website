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
        if form.is_valid():
            form.save()
            return success(request, form)
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

def success(request, form):
    if request.method == 'GET':
        return redirect('app_tesis:person_form')
    elif request.method == 'POST':
        ocean_answers = {key: value for key, value in form.cleaned_data.items() if key.startswith('ext') or key.startswith('est') or key.startswith('agr') or key.startswith('csn') or key.startswith('opn')}

        ocean_results = calculate_ocean(ocean_answers)

        return render(request, 'success.html', {'ocean_results': ocean_results})
    
def calculate_ocean(answers):
    # first re-encoding reverse items

    answers['ext2'] = 6 - answers['ext2']
    answers['ext4'] = 6 - answers['ext4']
    answers['ext6'] = 6 - answers['ext6']
    answers['ext8'] = 6 - answers['ext8']
    answers['ext10'] = 6 - answers['ext10']
    answers['est2'] = 6 - answers['est2']
    answers['est4'] = 6 - answers['est4']
    answers['agr1'] = 6 - answers['agr1']
    answers['agr3'] = 6 - answers['agr3']
    answers['agr5'] = 6 - answers['agr5']
    answers['agr7'] = 6 - answers['agr7']
    answers['csn2'] = 6 - answers['csn2']
    answers['csn4'] = 6 - answers['csn4']
    answers['csn6'] = 6 - answers['csn6']
    answers['csn8'] = 6 - answers['csn8']
    answers['opn2'] = 6 - answers['opn2']
    answers['opn4'] = 6 - answers['opn4']
    answers['opn6'] = 6 - answers['opn6']

    # then calculating the OCEAN scores
    extraversion = (answers['ext1'] + answers['ext2'] + answers['ext3'] + answers['ext4'] + answers['ext5'] + answers['ext6'] + answers['ext7'] + answers['ext8'] + answers['ext9'] + answers['ext10']) * 2
    neuroticism = (answers['est1'] + answers['est2'] + answers['est3'] + answers['est4'] + answers['est5'] + answers['est6'] + answers['est7'] + answers['est8'] + answers['est9'] + answers['est10']) * 2
    agreeableness = (answers['agr1'] + answers['agr2'] + answers['agr3'] + answers['agr4'] + answers['agr5'] + answers['agr6'] + answers['agr7'] + answers['agr8'] + answers['agr9'] + answers['agr10']) * 2
    conscientiousness = (answers['csn1'] + answers['csn2'] + answers['csn3'] + answers['csn4'] + answers['csn5'] + answers['csn6'] + answers['csn7'] + answers['csn8'] + answers['csn9'] + answers['csn10']) * 2
    openness = (answers['opn1'] + answers['opn2'] + answers['opn3'] + answers['opn4'] + answers['opn5'] + answers['opn6'] + answers['opn7'] + answers['opn8'] + answers['opn9'] + answers['opn10']) * 2

    ocean_results = {'extraversion': extraversion, 'neuroticism': neuroticism, 'agreeableness': agreeableness, 'conscientiousness': conscientiousness, 'openness': openness}

    return ocean_results