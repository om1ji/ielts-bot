# LINKS
speaking_club_google_forms = "https://example.com"
how_answer = "https://example.com"

# SUBSCRIPTION PRICE
price = "39 000"

welcome = {
    "text": 'Рады видеть вас!\nМы поможем подготовиться к IELTS.\n\nПодробный ответ на вопрос "Как?"\n{}\n\nЦена подписки: {} сум в месяц.\nСпособы оплаты: Payme, Click, Stripe'.format(
        how_answer, price
    )
}

not_subscribed = "У вас нет подписки. Оформите подписку"

pay_button = "Подписаться"

main_menu = {
    "text": "Главное меню",
    "tests": "Тесты",
    "services": "Сервисы",
    "settings": "Настройки",
}


# TESTS

tests_menu = {
    "text": "Меню тестов",
    "tests": "Задания на сегодня",
    "answers": "Ответы на задания",
}


# SERVICES

services_menu = {
    "text": "Меню Сервисов",
    "speaking_club": "Speaking Club",
    "writing_checker": "Writing Checker",
    "feed": "Персональная рассылка",
}

speaking_club = {
    "text": "Наш Speaking клуб пока проводится в тестовом формате\n\nДля участие заполните форму по ссылке:\n{}\n\nМы сами свяжемся с вами".format(
        speaking_club_google_forms
    ),
}

writing_checker_menu = {
    "text": "Проверь свой эссе",
    "part_1": "Part 1",
    "part_2": "Part 2",
    "send_text": "Отправьте ваше эссе в текстовом виде",
}

feed_menu = {
    "text": services_menu["feed"],
    "news": "Новости",
    "sites": "Сайты",
    "podcasts": "Подкасты",
}

# SETTINGS

settings_menu = {"text": "Настройки", "language": "Язык", "subscription": "Подписка"}
language_menu = {
    "text": "Выберите язык",
    "en": "Английский",
    "ru": "Русский",
    "uz": "Узбекский",
}

languages = ["en", "ru", "uz"]

language_changed = "Язык измененён на Русский"

# MENU

menu_back = "Назад"

# UNSUBSCRIBED

unsubscribed = "Ваша подписка кончилась"
