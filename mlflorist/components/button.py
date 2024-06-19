import reflex as rx
from mlflorist.components.text import texts


def button(text: str, size: str, size_border="", color="") -> rx.Component:
    return rx.button(
        texts(text, size=size),
        border=f"{size_border} solid {color}" if size_border and color else ""
    )
