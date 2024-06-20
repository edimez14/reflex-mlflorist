import reflex as rx
from mlflorist.data import Service
from mlflorist.styles.styles import IMAGE_HEIGHT, EmSize, Size, glassmorphism


def card_detail(service: Service) -> rx.Component:
    return rx.card(
        rx.box(
            rx.inset(
                rx.image(
                    src=service.image,
                    height="300px",
                    width="100%",
                    object_fit="cover"
                ),
                side="top",
                pb="current",
            ),
            rx.text.strong(service.title),
            rx.text(
                service.description,
                size=Size.SMALL.value,
                color_scheme="gray",
            ),
            spacing=Size.MEDIUM.value,
        ),
        style=glassmorphism,
        width="100%",
        variant="ghost",
    )
