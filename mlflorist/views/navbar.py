import reflex as rx
from mlflorist import data
from mlflorist.styles.styles import Colors, EmSize, Size, glassmorphism
from mlflorist.components.text import texts
from mlflorist.components.media import media

DATA = data.data

def navbar() -> rx.Component:
    return rx.vstack(
        rx.mobile_only(
            rx.hstack(
                # rx.image(DATA.logo, ),
                texts("MLflorist", Size.SXSMALL.value),
                media(DATA.media),
                rx.spacer(),
                rx.link(texts("Inicio", Size.SXSMALL.value), href="#"),
                rx.link(texts("Sobre Mi", Size.SXSMALL.value), href="#"),
                rx.link(texts("Galeria", Size.SXSMALL.value), href="#"),
                style=glassmorphism,
                width="100%",
                padding_x=EmSize.DEFAULT.value,
                padding_y=EmSize.SMALL.value,
            ),
            width="100%",
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                # rx.image(DATA.logo, ),
                texts("MLflorist", Size.SMALL.value),
                media(DATA.media),
                rx.spacer(),
                rx.link(texts("Inicio", Size.SMALL.value), href="#"),
                rx.link(texts("Sobre Mi", Size.SMALL.value), href="#"),
                rx.link(texts("Galeria", Size.SMALL.value), href="#"),
                style=glassmorphism,
                width="100%",
                padding_x=EmSize.DEFAULT.value,
                padding_y=EmSize.SMALL.value,
            ),
            width="100%",
        ),
        padding_x=EmSize.DEFAULT.value,
        padding_y=EmSize.DEFAULT.value,
        position="absolute",
        width="100%",
    )
