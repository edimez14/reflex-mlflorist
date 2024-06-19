import reflex as rx
from rxconfig import config
from mlflorist import data
from mlflorist.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size, glassmorphism, Colors
from mlflorist.views.navbar import navbar
from mlflorist.views.header import header
from mlflorist.views.info import info

DATA = data.data


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.center(
            rx.vstack(
                header(DATA.header),
                rx.center(
                    rx.vstack(
                        info("Experiencia", DATA.experience),
                    ),
                    max_width=MAX_WIDTH,
                    width="100%",
                    spacing=Size.XBIG.value,
                    padding_x=EmSize.DEFAULT.value,
                    padding_y=EmSize.DEFAULT.value,
                ),
            ),
            width="100%",
            as_child=True,
            spacing=Size.XBIG.value,
        ),
        # width="100%",
        spacing=Size.XBIG.value,  
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style={
        **BASE_STYLE,
        "background": Colors.floralwhite.value,
        "color": Colors.black.value,
    },
    theme=rx.theme(
        accent_color="pink",
        radius="medium"
    ),
)

title = DATA.title
description = DATA.description
logo = DATA.logo

app.add_page(
    index,
    title=title,
    description=description,
    image=logo,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": logo}
    ]
)
