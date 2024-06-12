import json

class Media:
    def __init__(self, email, twitter, tiktok, instagram, pinterest, likedin):
        self.email = email
        self.twitter = twitter
        self.tiktok = tiktok
        self.instagram = instagram
        self.pinterest = pinterest
        self.likedin = likedin

class Header:
    def __init__(self, image, title, about, button):
        self.image = image
        self.title = title
        self.about = about
        self.button = button

class Experience:
    def __init__(self, title, subtitle, description, date):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date

class Service:
    def __init__(self, image, title, description):
        self.image = image
        self.title = title
        self.description = description

class Galery:
    def __init__(self, image_1, image_2, image_3, image_4, image_5, button):
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3
        self.image_4 = image_4
        self.image_5 = image_5
        self.button = button

class Footer:
    def __init__(self, description, button_whatsapp, title, copyright):
        self.description = description
        self.button_whatsapp = button_whatsapp
        self.title = title
        self.copyright = copyright

class Data:
    def __init__(self, title, description, logo, media, header, experience, services, galery, footer):
        self.title = title
        self.description = description
        self.logo = logo
        self.media = Media(**media)
        self.header = Header(**header)
        self.experience = [Experience(**exp) for exp in experience]
        self.services = [Service(**srv) for srv in services]
        self.galery = Galery(**galery)
        self.footer = Footer(**footer)

# Leer el archivo JSON
with open("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)

