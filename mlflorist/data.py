import json


class MediaItem:
    def __init__(self, icon, url):
        self.icon = icon
        self.url = url


class Media:
    def __init__(self, email, twitter, tiktok, instagram, pinterest, likedin):
        self.email = MediaItem(**email)
        self.twitter = MediaItem(**twitter)
        self.tiktok = MediaItem(**tiktok)
        self.instagram = MediaItem(**instagram)
        self.pinterest = MediaItem(**pinterest)
        self.likedin = MediaItem(**likedin)


class Header:
    def __init__(self, image, title, about, button):
        self.image = image
        self.title = title
        self.about = about
        self.button = button


class ExperienceItem:
    def __init__(self, image, title, subtitle, description, date):
        self.image = image
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date


class Experience:
    def __init__(self, experience_1, experience_2, experience_3):
        self.experience_1 = ExperienceItem(**experience_1)
        self.experience_2 = ExperienceItem(**experience_2)
        self.experience_3 = ExperienceItem(**experience_3)


class Service:
    def __init__(self, image, title, description):
        self.image = image
        self.title = title
        self.description = description


class Gallery:
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
        self.experience = Experience(**experience)
        self.services = [Service(**srv) for srv in services]
        self.gallery = Galery(**gallery)
        self.footer = Footer(**footer)


# Leer el archivo JSON
with open("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)