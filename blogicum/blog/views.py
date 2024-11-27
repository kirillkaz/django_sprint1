from django.http import HttpRequest
from django.shortcuts import HttpResponse, render


class UndefinedPostIndexError(ValueError):
    pass


posts = [
    {
        "id": 0,
        "location": "Остров отчаянья",
        "date": "30 сентября 1659 года",
        "category": "travel",
        "text": """Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.""",
    },
    {
        "id": 1,
        "location": "Остров отчаянья",
        "date": "1 октября 1659 года",
        "category": "not-my-day",
        "text": """Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.""",
    },
    {
        "id": 2,
        "location": "Остров отчаянья",
        "date": "25 октября 1659 года",
        "category": "not-my-day",
        "text": """Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.""",
    },
]


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    template_name = "blog/index.html"

    context = {
        "posts": posts,
    }

    return render(request, template_name, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template_name = "blog/detail.html"

    post = None
    for elem in posts:
        if id == elem["id"]:
            post = elem
            break

    if post is None:
        raise UndefinedPostIndexError(f"Error. Post with {id=} was not found.")

    context = {
        "post": post,
    }

    return render(request, template_name, context)


def category(request: HttpRequest, category_slug: str) -> HttpResponse:
    template_name = "blog/category.html"

    context = {
        "category_slug": category_slug,
    }

    return render(request, template_name, context)
