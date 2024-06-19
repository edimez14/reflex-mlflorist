import reflex as rx
from mlflorist.components.boxicon import boxicon

def icon_link(icon: str, url: str, text="",) -> rx.Component:
    return rx.link(
        rx.mobile_only(
            boxicon(icon, "15px"),
            text,
        ),
        rx.tablet_and_desktop(
            boxicon(icon, "20px"),
            text,
        ),
        href=url,
        is_external=True
    )
