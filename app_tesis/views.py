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

    extraversion_score = (answers['ext1'] + answers['ext2'] + answers['ext3'] + answers['ext4'] + answers['ext5'] + answers['ext6'] + answers['ext7'] + answers['ext8'] + answers['ext9'] + answers['ext10']) * 2
    neuroticism_score = (answers['est1'] + answers['est2'] + answers['est3'] + answers['est4'] + answers['est5'] + answers['est6'] + answers['est7'] + answers['est8'] + answers['est9'] + answers['est10']) * 2
    agreeableness_score = (answers['agr1'] + answers['agr2'] + answers['agr3'] + answers['agr4'] + answers['agr5'] + answers['agr6'] + answers['agr7'] + answers['agr8'] + answers['agr9'] + answers['agr10']) * 2
    conscientiousness_score = (answers['csn1'] + answers['csn2'] + answers['csn3'] + answers['csn4'] + answers['csn5'] + answers['csn6'] + answers['csn7'] + answers['csn8'] + answers['csn9'] + answers['csn10']) * 2
    openness_score = (answers['opn1'] + answers['opn2'] + answers['opn3'] + answers['opn4'] + answers['opn5'] + answers['opn6'] + answers['opn7'] + answers['opn8'] + answers['opn9'] + answers['opn10']) * 2

    extraversion_info = 'Extraversión es una dimensión de la personalidad que describe el nivel de interacción que una persona tiene con su entorno. Las personas extrovertidas son sociables, amigables y habladoras, mientras que las personas introvertidas son reservadas, tranquilas y discretas.'
    neuroticism_info = 'Neuroticismo es una dimensión de la personalidad que describe el nivel de estabilidad emocional y control de impulsos de una persona. Las personas con alto nivel de neuroticismo son más propensas a experimentar emociones negativas, como ansiedad, depresión o ira, mientras que las personas con bajo nivel de neuroticismo son más propensas a experimentar emociones positivas, como calma, tranquilidad o felicidad.'
    agreeableness_info = 'Amabilidad es una dimensión de la personalidad que describe el nivel de empatía y cooperación de una persona. Las personas con alto nivel de amabilidad son más propensas a ser altruistas, comprensivas y generosas, mientras que las personas con bajo nivel de amabilidad son más propensas a ser competitivas, desconfiadas y egoístas.'
    conscientiousness_info = 'Responsabilidad es una dimensión de la personalidad que describe el nivel de organización y disciplina de una persona. Las personas con alto nivel de responsabilidad son más propensas a ser ordenadas, planificadas y disciplinadas, mientras que las personas con bajo nivel de responsabilidad son más propensas a ser desorganizadas, espontáneas y desordenadas.'
    openness_info = 'Apertura es una dimensión de la personalidad que describe el nivel de apertura mental y curiosidad de una persona. Las personas con alto nivel de apertura son más propensas a ser creativas, imaginativas y curiosas, mientras que las personas con bajo nivel de apertura son más propensas a ser convencionales, tradicionales y conservadoras.'

    extraversion_score_description = { 
        'very_low': 'Tu puntuación en extraversión es muy baja. Prefieres actividades solitarias y puedes ser introvertido en situaciones sociales. Disfrutas del tiempo a solas y puedes ser reservado.',
        'low': 'Tu puntuación en extraversión es baja. Eres capaz de disfrutar de la compañía de otros, pero también valoras tu tiempo a solas. Puedes ser tanto introvertido como extrovertido en diferentes situaciones.',
        'medium': 'Tu puntuación en extraversión es moderada. Disfrutas de las interacciones sociales, pero también valoras tu tiempo a solas. Puedes adaptarte fácilmente a diferentes entornos sociales.',
        'high': 'Tu puntuación en extraversión es alta. Eres extrovertido y disfrutas de la compañía de otras personas. Tienes una personalidad sociable y te sientes cómodo en situaciones sociales.',
        'very_high': 'Tu puntuación en extraversión es muy alta. Eres extremadamente extrovertido y te encanta interactuar con otras personas. Disfrutas de la compañía social y puedes ser el alma de la fiesta.'
    }

    neuroticism_score_description = { 
        'very_low': 'Tu puntuación en neuroticismo es muy baja. Eres generalmente calmado y resistente al estrés. Tienes una tendencia a experimentar emociones positivas y a mantener la serenidad en situaciones desafiantes.',
        'low': 'Tu puntuación en neuroticismo es baja. Eres emocionalmente estable en la mayoría de las situaciones, pero ocasionalmente puedes experimentar estrés o ansiedad moderados.',
        'medium': 'Tu puntuación en neuroticismo es moderada. Tienes una buena capacidad para manejar el estrés y las emociones negativas, pero ocasionalmente puedes sentirte ansioso o preocupado.',
        'high': 'Tu puntuación en neuroticismo es alta. Puedes ser propenso a experimentar estrés, ansiedad y emociones negativas en situaciones desafiantes. Practicar técnicas de manejo del estrés podría ser beneficioso para ti.',
        'very_high': 'Tu puntuación en neuroticismo es muy alta. Experimentas emociones negativas con frecuencia y puedes ser sensible al estrés. Es importante buscar formas efectivas de gestionar el estrés y cuidar tu bienestar emocional.'
    }

    agreeableness_score_description = { 
        'very_low': 'Tu puntuación en amabilidad es muy baja. Esto sugiere que puedes ser crítico y competitivo en lugar de cooperativo. Es posible que tiendas a enfocarte más en tus propios intereses que en los demás.',
        'low': 'Tu puntuación en amabilidad es baja. Eres capaz de ser cooperativo en ciertas situaciones, pero también puedes ser crítico o competitivo en otras.',
        'medium': 'Tu puntuación en amabilidad es moderada. Eres generalmente cooperativo y empático, pero también puedes establecer límites cuando es necesario.',
        'high': 'Tu puntuación en amabilidad es alta. Eres cooperativo, empático y generalmente dispuesto a ayudar a los demás. Te relacionas bien con los demás y valoras las relaciones armoniosas.',
        'very_high': 'Tu puntuación en amabilidad es muy alta. Eres extremadamente cooperativo, empático y siempre dispuesto a ayudar a los demás. Tu naturaleza amable y compasiva es una fortaleza en tus relaciones.'
    }

    conscientiousness_score_description = { 
        'very_low': 'Tu puntuación en consciencia es muy baja. Esto sugiere que puedes ser espontáneo y flexible en tu enfoque de la vida. Es posible que no pongas un fuerte énfasis en la organización y a veces tengas dificultades con los plazos y las responsabilidades.',
        'low': 'Tu puntuación en consciencia es baja. Aunque eres algo organizado, también puedes adaptarte a las circunstancias cambiantes. Puedes priorizar las tareas en función de su urgencia e importancia.',
        'medium': 'Tu puntuación en consciencia es moderada. Indica que eres organizado y responsable sin ser excesivamente rígido. Puedes encontrar un equilibrio entre la planificación y la flexibilidad, lo que te hace confiable en diversas situaciones.',
        'high': 'Tu puntuación en consciencia es alta. Excelentes en organización y responsabilidad, superando las expectativas. Eres diligente, disciplinado y reconocido por tu confiabilidad y compromiso con tus metas.',
        'very_high': 'Tu puntuación en consciencia es muy alta. Eres extremadamente organizado y responsable. Destacas en la organización y la responsabilidad, y a menudo superas las expectativas. Eres diligente, disciplinado y conocido por tu confiabilidad y compromiso con tus objetivos.'
    }

    openness_score_description = { 
        'very_low': 'Tu puntuación en apertura es muy baja. Esto sugiere que puedes preferir lo conocido y rutinario. Es posible que te sientas más cómodo con lo familiar y que tengas menos inclinación por explorar nuevas ideas o actividades no convencionales.',
        'low': 'Tu puntuación en apertura es baja. Aunque puedes ser algo abierto a nuevas experiencias, tiendes a mantener cierta rutina y comodidad en lo conocido.',
        'medium': 'Tu puntuación en apertura es moderada. Eres receptivo a nuevas ideas y experiencias, pero también encuentras valor en la estabilidad y lo familiar.',
        'high': 'Tu puntuación en apertura es alta. Buscas activamente oportunidades para explorar y abrazar nuevas perspectivas. Encuentras un equilibrio entre la rutina y la novedad.',
        'very_high': 'Tu puntuación en apertura es muy alta. Tienes un fuerte deseo de explorar nuevas ideas, culturas y experiencias. Disfrutas activamente buscando oportunidades para ampliar tus horizontes y eres abierto a ideas poco convencionales.'
    }

    score_ranges = {
        'very_low': (0, 20),
        'low': (21, 40),
        'medium': (41, 60),
        'high': (61, 80),
        'very_high': (81, 100)
    }

    ocean_results = {
        'oppenness': {
            'title': 'Apertura (Openness)', 
            'info': openness_info, 
            'score': openness_score, 
            'score_description': openness_score_description[get_score_range(openness_score, score_ranges)],
            'color': 'purple'
            },
        'conscientiousness': {
            'title': 'Responsabilidad (Conscientiousness)', 
            'info': conscientiousness_info, 
            'score': conscientiousness_score, 
            'score_description': conscientiousness_score_description[get_score_range(conscientiousness_score, score_ranges)],
            'color': 'blue'
            },
        'extraversion': {
            'title': 'Extraversión (Extraversion)', 
            'info': extraversion_info, 
            'score': extraversion_score, 
            'score_description': extraversion_score_description[get_score_range(extraversion_score, score_ranges)],
            'color': 'red'
            },
        'agreeableness': {
            'title': 'Amabilidad (Agreeableness)', 
            'info': agreeableness_info, 
            'score': agreeableness_score, 
            'score_description': agreeableness_score_description[get_score_range(agreeableness_score, score_ranges)],
            'color': 'green'
            },
        'neuroticism': {
            'title': 'Neuroticismo (Neuroticism)', 
            'info': neuroticism_info, 
            'score': neuroticism_score, 
            'score_description': neuroticism_score_description[get_score_range(neuroticism_score, score_ranges)],
            'color': 'yellow'
            }
        }

    return ocean_results

def get_score_range(score, ranges):
    for category, (min_score, max_score) in ranges.items():
        if min_score <= score <= max_score:
            return category
    return None


