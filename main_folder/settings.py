main_url = 'http://127.0.0.1:5000'
secret_key = 'your_mother'

def url_maker(url):
        return main_url+url

unicontext = {'menu': [
        {'name': 'Главная страница', 'url': url_maker('/')},
        {'name': 'Электронный журнал', 'url': url_maker('/elzhur')},        
],
'lower_menu': [
        {'name': 'Форма обратной связи', 'url': url_maker('/contact')},
        {'name': 'Об авторе', 'url': ''},
        {'name': 'О технологиях проекта', 'url': ''},        
]
}