import reflex as rx
# from mlflorist.styles.styles import Size


def texts(text: str, size="", color="") -> rx.Component:
    return rx.text(
        text,
        size=size,
        color=color,
        text_shadow="2px 2px 4px rgba(0, 0, 0, 0.5)"
    )
