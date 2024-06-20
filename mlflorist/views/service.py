import reflex as rx
from mlflorist.components.card_detail import card_detail
from mlflorist.components.heading import heading
from mlflorist.data import Service
from mlflorist.styles.styles import Size, EmSize


def service(services: list[Service]) -> rx.Component:
    return rx.vstack(
        heading("Service"),
        heading("What can i do?"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(service)
                    for service in services
                ],
                spacing=Size.BIG.value,
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(service)
                    for service in services
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        align="center",
        spacing=Size.MEDIUM.value,
        width="100%"
    )
