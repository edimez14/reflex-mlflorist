import reflex as rx
from mlflorist.components.boxicon import boxicon
from mlflorist.styles.styles import Colors


def icon_link(icon: str, url: str, footer=False, text="") -> rx.Component:
    return rx.link(
        rx.cond(
            footer == False,
            rx.box(
                rx.mobile_only(
                    boxicon(icon, "15px", Colors.hotpink.value),
                    text,
                ),
                rx.tablet_and_desktop(
                    boxicon(icon, "20px", Colors.hotpink.value),
                    text,
                ),
            ),
        ),
        rx.cond(
            footer == True,
            rx.box(
                rx.mobile_only(
                    boxicon(icon, "40px", Colors.hotpink.value),
                    text,
                ),
                rx.tablet_and_desktop(
                    boxicon(icon, "60px", Colors.hotpink.value),
                    text,
                ),
            ),
        ),
        href=url,
        is_external=True
    )
