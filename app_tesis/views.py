from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_protect
from django.utils import translation
from django.conf import settings
from django.http import HttpResponseRedirect

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/success/'
    template_name = 'person_form.html'

def switch_language(request, language):
    if language in ['es', 'en', 'it', 'fr', 'ca']:
        translation.activate(language)
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        translation.activate('en')
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'en')

    return response

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
    
    if translation.get_language() == 'es':
        file = open('preguntas_es.txt', 'r')
        questions = file.readlines()
        file.close()
    elif translation.get_language() == 'en':
        file = open('preguntas_en.txt', 'r')
        questions = file.readlines()
        file.close()
    elif translation.get_language() == 'it':
        file = open('preguntas_it.txt', 'r')
        questions = file.readlines()
        file.close()
    elif translation.get_language() == 'fr':
        file = open('preguntas_fr.txt', 'r')
        questions = file.readlines()
        file.close()
    elif translation.get_language() == 'ca':
        file = open('preguntas_ca.txt', 'r')
        questions = file.readlines()
        file.close()
    else:
        file = open('preguntas_en.txt', 'r')
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

        ocean_results = calculate_ocean(request, ocean_answers)

        return render(request, 'success.html', {'ocean_results': ocean_results})
    
def calculate_ocean(request, answers):
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

    if translation.get_language() == 'es':
        extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description = get_spanish_texts()
    elif translation.get_language() == 'en':
        extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description = get_english_texts()
    elif translation.get_language() == 'it':
        extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description = get_italian_texts()
    elif translation.get_language() == 'fr':
        extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description = get_french_texts()
    elif translation.get_language() == 'ca':
        extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description = get_catalan_texts()
    else:
        extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description = get_english_texts()

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


def get_spanish_texts():
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

    return extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description

def get_english_texts():
    extraversion_info = "Extraversion is a personality dimension that describes the level of interaction a person has with their environment. Extraverted individuals are sociable, friendly, and talkative, while introverted individuals are reserved, quiet, and discreet."
    neuroticism_info = "Neuroticism is a personality dimension that describes the level of emotional stability and impulse control of a person. Individuals with a high level of neuroticism are more prone to experiencing negative emotions such as anxiety, depression, or anger, while those with a low level of neuroticism are more likely to experience positive emotions like calmness, tranquility, or happiness."
    agreeableness_info = "Agreeableness is a personality dimension that describes a person's level of empathy and cooperation. Individuals with a high level of agreeableness are more likely to be altruistic, understanding, and generous, while those with a low level of agreeableness are more prone to being competitive, distrustful, and selfish."
    conscientiousness_info = "Conscientiousness is a personality dimension that describes a person's level of organization and discipline. Individuals with a high level of conscientiousness are more likely to be orderly, planned, and disciplined, while those with a low level of conscientiousness are more prone to being disorganized, spontaneous, and disorderly."
    openness_info = "Openness is a personality dimension that describes a person's level of mental openness and curiosity. Individuals with a high level of openness are more likely to be creative, imaginative, and curious, while those with a low level of openness are more prone to being conventional, traditional, and conservative."

    extraversion_score_description = { 
        "very_low": "Your extraversion score is very low. You prefer solitary activities and can be introverted in social situations. You enjoy alone time and can be reserved.",
        "low": "Your extraversion score is low. You can enjoy the company of others, but also value your alone time. You can be both introverted and extroverted in different situations.",
        "medium": "Your extraversion score is moderate. You enjoy social interactions but also value your alone time. You can easily adapt to different social environments.",
        "high": "Your extraversion score is high. You are extroverted and enjoy the company of other people.",
        "very_high": "Your extraversion score is very high. You are extremely extroverted and love interacting with other people. You enjoy social company and can be the life of the party."
    }

    neuroticism_score_description = { 
        "very_low": "Your neuroticism score is very low. You are generally calm and resilient to stress. You have a tendency to experience positive emotions and maintain serenity in challenging situations.",
        "low": "Your neuroticism score is low. You are emotionally stable in most situations, but occasionally, you may experience moderate stress or anxiety.",
        "medium": "Your neuroticism score is moderate. You have good stress management and can handle negative emotions, but occasionally, you may feel anxious or worried.",
        "high": "Your neuroticism score is high. You may be prone to experiencing stress, anxiety, and negative emotions in challenging situations. Practicing stress management techniques could be beneficial for you.",
        "very_high": "Your neuroticism score is very high. You frequently experience negative emotions and can be sensitive to stress. It's important to seek effective ways to manage stress and take care of your emotional well-being."
    }

    agreeableness_score_description = { 
        "very_low": "Your agreeableness score is very low. This suggests you can be critical and competitive rather than cooperative. You may tend to focus more on your own interests than on others.",
        "low": "Your agreeableness score is low. You are capable of being cooperative in certain situations, but you can also be critical or competitive in others.",
        "medium": "Your agreeableness score is moderate. You are generally cooperative and empathetic, but you can also set boundaries when necessary.",
        "high": "Your agreeableness score is high. You are cooperative, empathetic, and generally willing to help others. You get along well with others and value harmonious relationships.",
        "very_high": "Your agreeableness score is very high. You are extremely cooperative, empathetic, and always willing to help others. Your kind and compassionate nature is a strength in your relationships."
    }

    conscientiousness_score_description = { 
        "very_low": "Your conscientiousness score is very low. This suggests you can be spontaneous and flexible in your approach to life. You may not place a strong emphasis on organization and may sometimes struggle with deadlines and responsibilities.",
        "low": "Your conscientiousness score is low. Although you are somewhat organized, you can also adapt to changing circumstances. You can prioritize tasks based on their urgency and importance.",
        "medium": "Your conscientiousness score is moderate. It indicates that you are organized and responsible without being overly rigid. You can find a balance between planning and flexibility, making you reliable in various situations.",
        "high": "Your conscientiousness score is high. You excel in organization and responsibility, exceeding expectations. You are diligent, disciplined, and recognized for your reliability and commitment to your goals.",
        "very_high": "Your conscientiousness score is very high. You are extremely organized and responsible. You stand out in organization and responsibility and often exceed expectations. You are diligent, disciplined, and known for your reliability and commitment to your objectives."
    }

    openness_score_description = { 
        "very_low": "Your openness score is very low. This suggests you may prefer the known and routine. You may feel more comfortable with the familiar and have less inclination to explore new ideas or unconventional activities.",
        "low": "Your openness score is low. Although you can be somewhat open to new experiences, you tend to maintain a certain routine and comfort in the known.",
        "medium": "Your openness score is moderate. You are receptive to new ideas and experiences, but you also find value in stability and the familiar.",
        "high": "Your openness score is high. You actively seek opportunities to explore and embrace new perspectives. You strike a balance between routine and novelty.",
        "very_high": "Your openness score is very high. You have a strong desire to explore new ideas, cultures, and experiences. You actively enjoy seeking opportunities to broaden your horizons and are open to unconventional ideas."
    }

    return extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description

def get_italian_texts():
    extraversion_info = "L'Estroversione è una dimensione della personalità che descrive il livello di interazione che una persona ha con il proprio ambiente. Le persone estroverse sono socievoli, amichevoli e loquaci, mentre le persone introverso sono riservate, tranquille e discrete."
    neuroticism_info = "Il Neuroticismo è una dimensione della personalità che descrive il livello di stabilità emotiva e il controllo degli impulsi di una persona. Le persone con un alto livello di neuroticismo sono più inclini a sperimentare emozioni negative come ansia, depressione o rabbia, mentre le persone con un basso livello di neuroticismo sono più propense a sperimentare emozioni positive come calma, tranquillità o felicità."
    agreeableness_info = "L'Accordabilità è una dimensione della personalità che descrive il livello di empatia e cooperazione di una persona. Le persone con un alto livello di accordabilità sono più propense ad essere altruiste, comprensive e generose, mentre le persone con un basso livello di accordabilità sono più propense a essere competitive, diffidenti ed egoiste."
    conscientiousness_info = "La Coscienziosità è una dimensione della personalità che descrive il livello di organizzazione e disciplina di una persona. Le persone con un alto livello di coscienziosità sono più propense a essere ordinate, pianificate e disciplinate, mentre le persone con un basso livello di coscienziosità sono più propense a essere disordinate, spontanee e trasandate."
    openness_info = "L'Apertura è una dimensione della personalità che descrive il livello di apertura mentale e curiosità di una persona. Le persone con un alto livello di apertura sono più propense a essere creative, imaginative e curiose, mentre le persone con un basso livello di apertura sono più propense a essere conservative, tradizionali e convenzionali."

    extraversion_score_description = { 
        'very_low': "Il tuo punteggio di estroversione è molto basso. Preferisci attività solitarie e puoi essere introverso in situazioni sociali. Apprezzi il tempo da solo e puoi essere riservato.",
        'low': "Il tuo punteggio di estroversione è basso. Sei in grado di goderti la compagnia degli altri, ma apprezzi anche il tuo tempo da solo. Puoi essere sia introverso che estroverso in diverse situazioni.",
        'medium': "Il tuo punteggio di estroversione è moderato. Apprezzi le interazioni sociali, ma valorizzi anche il tuo tempo da solo. Puoi adattarti facilmente a diversi contesti sociali.",
        'high': "Il tuo punteggio di estroversione è alto. Sei estroverso e apprezzi la compagnia delle altre persone. Hai una personalità socievole e ti senti a tuo agio in situazioni sociali.",
        'very_high': "Il tuo punteggio di estroversione è molto alto. Sei estremamente estroverso e ami interagire con altre persone. Apprezzi la compagnia sociale e puoi essere l'anima della festa."
    }

    neuroticism_score_description = { 
        'very_low': "Il tuo punteggio di neuroticismo è molto basso. Sei generalmente calmo e resiliente allo stress. Hai la tendenza a sperimentare emozioni positive e a mantenere la serenità in situazioni sfidanti.",
        'low': "Il tuo punteggio di neuroticismo è basso. Sei emotivamente stabile nella maggior parte delle situazioni, ma occasionalmente puoi sperimentare stress o ansia moderati.",
        'medium': "Il tuo punteggio di neuroticismo è moderato. Hai una buona capacità di gestire lo stress e le emozioni negative, ma occasionalmente puoi sentirti ansioso o preoccupato.",
        'high': "Il tuo punteggio di neuroticismo è alto. Puoi essere incline a sperimentare stress, ansia ed emozioni negative in situazioni sfidanti. Praticare tecniche di gestione dello stress potrebbe essere benefico per te.",
        'very_high': "Il tuo punteggio di neuroticismo è molto alto. Sperimenti frequentemente emozioni negative e puoi essere sensibile allo stress. È importante cercare modi efficaci per gestire lo stress e prendersi cura del tuo benessere emotivo."
    }

    agreeableness_score_description = { 
        'very_low': "Il tuo punteggio di accordabilità è molto basso. Questo suggerisce che puoi essere critico e competitivo anziché cooperativo. Potresti tendere a concentrarti di più sui tuoi interessi che sugli interessi degli altri.",
        'low': "Il tuo punteggio di accordabilità è basso. Sei in grado di essere cooperativo in alcune situazioni, ma puoi anche essere critico o competitivo in altre.",
        'medium': "Il tuo punteggio di accordabilità è moderato. Sei generalmente cooperativo ed empatico, ma puoi anche stabilire limiti quando è necessario.",
        'high': "Il tuo punteggio di accordabilità è alto. Sei cooperativo, empatico e generalmente disposto ad aiutare gli altri. Ti relazioni bene con gli altri e valorizzi relazioni armoniose.",
        'very_high': "Il tuo punteggio di accordabilità è molto alto. Sei estremamente cooperativo, empatico e sempre pronto ad aiutare gli altri. La tua natura gentile e compassionevole è un punto di forza nelle tue relazioni."
    }

    conscientiousness_score_description = { 
        'very_low': "Il tuo punteggio di coscienziosità è molto basso. Questo suggerisce che puoi essere spontaneo e flessibile nel tuo approccio alla vita. Potresti non porre un forte accento sull'organizzazione e talvolta potresti avere difficoltà con scadenze e responsabilità.",
        'low': "Il tuo punteggio di coscienziosità è basso. Sebbene tu sia in qualche modo organizzato, puoi anche adattarti a circostanze mutevoli. Puoi dare priorità alle attività in base all'urgenza e all'importanza.",
        'medium': "Il tuo punteggio di coscienziosità è moderato. Indica che sei organizzato e responsabile senza essere eccessivamente rigido. Puoi trovare un equilibrio tra la pianificazione e la flessibilità, rendendoti affidabile in varie situazioni.",
        'high': "Il tuo punteggio di coscienziosità è alto. Eccelli nell'organizzazione e nella responsabilità, superando le aspettative. Sei diligente, disciplinato e riconosciuto per la tua affidabilità e il tuo impegno verso i tuoi obiettivi.",
        'very_high': "Il tuo punteggio di coscienziosità è molto alto. Sei estremamente organizzato e responsabile. Ti distingui nell'organizzazione e nella responsabilità e spesso superi le aspettative. Sei diligente, disciplinato e noto per la tua affidabilità e il tuo impegno verso i tuoi obiettivi."
    }

    openness_score_description = { 
        'very_low': "Il tuo punteggio di apertura è molto basso. Questo suggerisce che potresti preferire ciò che è noto e abituale. Potresti sentirti più a tuo agio con ciò che è familiare e avere meno inclinazione a esplorare nuove idee o attività non convenzionali.",
        'low': "Il tuo punteggio di apertura è basso. Sebbene tu possa essere in qualche modo aperto a nuove esperienze, tendi a mantenere una certa routine e comfort nella familiarità.",
        'medium': "Il tuo punteggio di apertura è moderato. Sei aperto a nuove idee ed esperienze, ma trovi anche valore nella stabilità e nella familiarità.",
        'high': "Il tuo punteggio di apertura è alto. Cerchi attivamente opportunità per esplorare e abbracciare nuove prospettive. Trovi un equilibrio tra routine e novità.",
        'very_high': "Il tuo punteggio di apertura è molto alto. Hai una forte volontà di esplorare nuove idee, culture ed esperienze. Cerchi attivamente opportunità per ampliare i tuoi orizzonti ed essere aperto a idee non convenzionali."
    }

    return extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description

def get_french_texts():
    extraversion_info = "L'extraversion est une dimension de la personnalité qui décrit le niveau d'interaction d'une personne avec son environnement. Les individus extravertis sont sociables, amicaux et bavards, tandis que les individus introvertis sont réservés, calmes et discrets."
    neuroticism_info = "Le névrotisme est une dimension de la personnalité qui décrit le niveau de stabilité émotionnelle et de contrôle des impulsions d'une personne. Les individus ayant un niveau élevé de névrotisme sont plus enclins à éprouver des émotions négatives telles que l'anxiété, la dépression ou la colère, tandis que ceux ayant un faible niveau de névrotisme sont plus susceptibles d'éprouver des émotions positives telles que le calme, la tranquillité ou le bonheur."
    agreeableness_info = "L'agrément est une dimension de la personnalité qui décrit le niveau d'empathie et de coopération d'une personne. Les individus ayant un niveau élevé d'agrément sont plus enclins à être altruistes, compréhensifs et généreux, tandis que ceux ayant un faible niveau d'agrément sont plus enclins à être compétitifs, méfiants et égoïstes."
    conscientiousness_info = "La conscience est une dimension de la personnalité qui décrit le niveau d'organisation et de discipline d'une personne. Les individus ayant un niveau élevé de conscience sont plus enclins à être ordonnés, planifiés et disciplinés, tandis que ceux ayant un faible niveau de conscience sont plus enclins à être désorganisés, spontanés et négligés."
    openness_info = "L'ouverture est une dimension de la personnalité qui décrit le niveau d'ouverture mentale et de curiosité d'une personne. Les individus ayant un niveau élevé d'ouverture sont plus enclins à être créatifs, imaginatifs et curieux, tandis que ceux ayant un faible niveau d'ouverture sont plus enclins à être conventionnels, traditionnels et conservateurs."

    extraversion_score_description = { 
        'very_low': "Votre score d'extraversion est très faible. Vous préférez les activités solitaires et pouvez être introverti dans des situations sociales. Vous appréciez le temps passé seul et pouvez être réservé.",
        'low': "Votre score d'extraversion est faible. Vous pouvez apprécier la compagnie des autres, mais vous valorisez également votre temps en solitaire. Vous pouvez être à la fois introverti et extraverti dans différentes situations.",
        'medium': "Votre score d'extraversion est modéré. Vous appréciez les interactions sociales, mais vous valorisez également votre temps en solitaire. Vous pouvez vous adapter facilement à différents environnements sociaux.",
        'high': "Votre score d'extraversion est élevé. Vous êtes extraverti et appréciez la compagnie des autres. Vous avez une personnalité sociable et vous vous sentez à l'aise dans des situations sociales.",
        'very_high': "Votre score d'extraversion est très élevé. Vous êtes extrêmement extraverti et adorez interagir avec d'autres personnes. Vous appréciez la compagnie sociale et pouvez être l'âme de la fête."
    }

    neuroticism_score_description = { 
        'very_low': "Votre score de névrotisme est très faible. Vous êtes généralement calme et résistant au stress. Vous avez tendance à éprouver des émotions positives et à maintenir la sérénité dans des situations difficiles.",
        'low': "Votre score de névrotisme est faible. Vous êtes émotionnellement stable dans la plupart des situations, mais pouvez parfois ressentir un stress ou une anxiété modérés.",
        'medium': "Votre score de névrotisme est modéré. Vous avez une bonne capacité à gérer le stress et les émotions négatives, mais pouvez parfois vous sentir anxieux ou inquiet.",
        'high': "Votre score de névrotisme est élevé. Vous pouvez être enclin à ressentir du stress, de l'anxiété et des émotions négatives dans des situations difficiles. La pratique de techniques de gestion du stress pourrait vous être bénéfique.",
        'very_high': "Votre score de névrotisme est très élevé. Vous ressentez fréquemment des émotions négatives et pouvez être sensible au stress. Il est important de chercher des moyens efficaces de gérer le stress et de prendre soin de votre bien-être émotionnel."
    }

    agreeableness_score_description = { 
        'very_low': "Votre score d'agrément est très faible. Cela suggère que vous pouvez être critique et compétitif plutôt que coopératif. Vous avez tendance à vous concentrer davantage sur vos propres intérêts que sur ceux des autres.",
        'low': "Votre score d'agrément est faible. Vous êtes capable d'être coopératif dans certaines situations, mais vous pouvez aussi être critique ou compétitif dans d'autres.",
        'medium': "Votre score d'agrément est modéré. Vous êtes généralement coopératif et empathique, mais vous pouvez aussi fixer des limites lorsque cela est nécessaire.",
        'high': "Votre score d'agrément est élevé. Vous êtes coopératif, empathique et généralement disposé à aider les autres. Vous vous entendez bien avec les autres et valorisez les relations harmonieuses.",
        'very_high': "Votre score d'agrément est très élevé. Vous êtes extrêmement coopératif, empathique et toujours prêt à aider les autres. Votre nature aimable et compatissante est une force dans vos relations."
    }

    conscientiousness_score_description = { 
        'very_low': "Votre score de conscience est très faible. Cela suggère que vous pouvez être spontané et flexible dans votre approche de la vie. Vous pourriez ne pas accorder une grande importance à l'organisation et avoir parfois des difficultés avec les délais et les responsabilités.",
        'low': "Votre score de conscience est faible. Bien que vous soyez quelque peu organisé, vous pouvez également vous adapter aux circonstances changeantes. Vous pouvez prioriser les tâches en fonction de leur urgence et de leur importance.",
        'medium': "Votre score de conscience est modéré. Il indique que vous êtes organisé et responsable sans être excessivement rigide. Vous pouvez trouver un équilibre entre la planification et la flexibilité, ce qui fait de vous une personne fiable dans diverses situations.",
        'high': "Votre score de conscience est élevé. Vous excellez dans l'organisation et la responsabilité, dépassant les attentes. Vous êtes diligent, discipliné et reconnu pour votre fiabilité et votre engagement envers vos objectifs.",
        'very_high': "Votre score de conscience est très élevé. Vous êtes extrêmement organisé et responsable. Vous vous démarquez dans l'organisation et la responsabilité, et dépassez souvent les attentes. Vous êtes diligent, discipliné et connu pour votre fiabilité et votre engagement envers vos objectifs."
    }

    openness_score_description = { 
        'very_low': "Votre score d'ouverture est très faible. Cela suggère que vous pourriez préférer le connu et la routine. Vous pourriez vous sentir plus à l'aise avec ce qui est familier et avoir moins de penchant pour explorer de nouvelles idées ou des activités non conventionnelles.",
        'low': "Votre score d'ouverture est faible. Bien que vous puissiez être quelque peu ouvert à de nouvelles expériences, vous avez tendance à maintenir une certaine routine et un certain confort dans ce qui est connu.",
        'medium': "Votre score d'ouverture est modéré. Vous êtes réceptif à de nouvelles idées et expériences, mais vous trouvez également de la valeur dans la stabilité et la familiarité.",
        'high': "Votre score d'ouverture est élevé. Vous recherchez activement des opportunités pour explorer et embrasser de nouvelles perspectives. Vous trouvez un équilibre entre la routine et la nouveauté.",
        'very_high': "Votre score d'ouverture est très élevé. Vous avez un fort désir d'explorer de nouvelles idées, cultures et expériences. Vous recherchez activement des opportunités pour élargir vos horizons et êtes ouvert à des idées non conventionnelles."
    }

    return extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description

def get_catalan_texts():
    extraversion_info = "L'extraversió és una dimensió de la personalitat que descriu el nivell d'interacció d'una persona amb el seu entorn. Les persones extravertides són sociables, amigables i parladores, mentre que les persones introvertides són reservades, tranquil·les i discretes."
    neuroticism_info = "El neurotisme és una dimensió de la personalitat que descriu el nivell d'estabilitat emocional i control d'impulsos d'una persona. Les persones amb un alt nivell de neurotisme són més propenses a experimentar emocions negatives com l'ansietat, la depressió o la ràbia, mentre que les persones amb un baix nivell de neurotisme són més propenses a experimentar emocions positives com la calma, la tranquil·litat o la felicitat."
    agreeableness_info = "La benevolència és una dimensió de la personalitat que descriu el nivell d'empatia i cooperació d'una persona. Les persones amb un alt nivell de benevolència són més propenses a ser altruistes, comprensius i generosos, mentre que les persones amb un baix nivell de benevolència són més propenses a ser competitives, desconfiades i egoistes."
    conscientiousness_info = "La responsabilitat és una dimensió de la personalitat que descriu el nivell d'organització i disciplina d'una persona. Les persones amb un alt nivell de responsabilitat són més propenses a ser ordenades, planificades i disciplinades, mentre que les persones amb un baix nivell de responsabilitat són més propenses a ser desorganitzades, espontànies i desordenades."
    openness_info = "L'obertura és una dimensió de la personalitat que descriu el nivell d'obertura mental i curiositat d'una persona. Les persones amb un alt nivell d'obertura són més propenses a ser creatives, imaginatives i curioses, mentre que les persones amb un baix nivell d'obertura són més propenses a ser convencionals, tradicionals i conservadores."

    extraversion_score_description = { 
        'very_low': "La teva puntuació en extraversió és molt baixa. Prefereixes activitats solitàries i pots ser introvertit en situacions socials. Gaudeixes del temps a soles i pots ser reservat.",
        'low': "La teva puntuació en extraversió és baixa. Ets capaç de gaudir de la companyia dels altres, però també values el teu temps a soles. Pots ser tant introvertit com extrovertit en diferents situacions.",
        'medium': "La teva puntuació en extraversió és moderada. Gaudeixes de les interaccions socials, però també values el teu temps a soles. Et pots adaptar fàcilment a diferents entorns socials.",
        'high': "La teva puntuació en extraversió és alta. Ets extrovertit i gaudeixes de la companyia d'altres persones. Tens una personalitat sociable i et sents còmode en situacions socials.",
        'very_high': "La teva puntuació en extraversió és molt alta. Ets extremadament extrovertit i t'encanta interactuar amb altres persones. Gaudeixes de la companyia social i pots ser l'ànima de la festa."
    }

    neuroticism_score_description = { 
        'very_low': "La teva puntuació en neurotisme és molt baixa. Ets generalment tranquil i resistent a l'estrès. Tens tendència a experimentar emocions positives i a mantenir la serenitat en situacions desafiants.",
        'low': "La teva puntuació en neurotisme és baixa. Ets emocionalment estable en la majoria de les situacions, però ocasionalment pots experimentar estrès o ansietat moderats.",
        'medium': "La teva puntuació en neurotisme és moderada. Tens una bona capacitat per gestionar l'estrès i les emocions negatives, però ocasionalment pots sentir-te ansios o preocupat.",
        'high': "La teva puntuació en neurotisme és alta. Pots ser propens a experimentar estrès, ansietat i emocions negatives en situacions desafiants. La pràctica de tècniques de gestió de l'estrès podria ser beneficiosa per a tu.",
        'very_high': "La teva puntuació en neurotisme és molt alta. Experimentes sovint emocions negatives i pots ser sensible a l'estrès. És important buscar maneres efectives de gestionar l'estrès i cuidar el teu benestar emocional."
    }

    agreeableness_score_description = { 
        'very_low': "La teva puntuació en benevolència és molt baixa. Això suggereix que pots ser crític i competitiu en lloc de cooperatiu. És possible que tendeixis a centrar-te més en els teus propis interessos que en els dels altres.",
        'low': "La teva puntuació en benevolència és baixa. Ets capaç de ser cooperatiu en determinades situacions, però també pots ser crític o competitiu en altres.",
        'medium': "La teva puntuació en benevolència és moderada. Ets generalment cooperatiu i empàtic, però també pots establir límits quan és necessari.",
        'high': "La teva puntuació en benevolència és alta. Ets cooperatiu, empàtic i generalment disposat a ajudar altres persones. Et relaciones bé amb els altres i values relacions harmonioses.",
        'very_high': "La teva puntuació en benevolència és molt alta. Ets extremadament cooperatiu, empàtic i sempre disposat a ajudar altres persones. La teva naturalesa amable i compassiva és una fortalesa en les teves relacions."
    }

    conscientiousness_score_description = { 
        'very_low': "La teva puntuació en responsabilitat és molt baixa. Això suggereix que pots ser espontani i flexible en la teva aproximació a la vida. És possible que no atorgis una gran importància a l'organització i tinguis, de tant en tant, dificultats amb els terminis i les responsabilitats.",
        'low': "La teva puntuació en responsabilitat és baixa. Tot i que ets una mica organitzat, també pots adaptar-te a les circumstàncies canviant. Pots prioritzar les tasques en funció de la seva urgència i importància.",
        'medium': "La teva puntuació en responsabilitat és moderada. Indica que ets organitzat i responsable sense ser excessivament rígid. Pots trobar un equilibri entre la planificació i la flexibilitat, la qual cosa et fa fiable en diferents situacions.",
        'high': "La teva puntuació en responsabilitat és alta. Ets excel·lent en organització i responsabilitat, superant les expectatives. Ets diligent, disciplinat i reconegut per la teva fiabilitat i el teu compromís amb els teus objectius.",
        'very_high': "La teva puntuació en responsabilitat és molt alta. Ets extremadament organitzat i responsable. Et destaquen en l'organització i la responsabilitat, i sovint superes les expectatives. Ets diligent, disciplinat i conegut per la teva fiabilitat i el teu compromís amb els teus objectius."
    }

    openness_score_description = { 
        'very_low': "La teva puntuació en obertura és molt baixa. Això suggereix que pots preferir el conegut i rutinari. És possible que et sentis més còmode amb el que és familiar i tinguis menys inclinació a explorar noves idees o activitats no convencionals.",
        'low': "La teva puntuació en obertura és baixa. Tot i que pots ser una mica obert a noves experiències, tends a mantenir certa rutina i comoditat en allò conegut.",
        'medium': "La teva puntuació en obertura és moderada. Ets receptiu a noves idees i experiències, però també hi trobes valor en la estabilitat i el conegut.",
        'high': "La teva puntuació en obertura és alta. Busques activament oportunitats per explorar i abraçar noves perspectives. Trobes un equilibri entre la rutina i la novetat.",
        'very_high': "La teva puntuació en obertura és molt alta. Tens un fort desig d'explorar noves idees, cultures i experiències. Gaudeixes activament cercant oportunitats per ampliar els teus horitzons i ets obert a idees no convencionals."
    }

    return extraversion_info, neuroticism_info, agreeableness_info, conscientiousness_info, openness_info, extraversion_score_description, neuroticism_score_description, agreeableness_score_description, conscientiousness_score_description, openness_score_description
