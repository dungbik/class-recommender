from django.apps import AppConfig



class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        print("처음만 실행")
