import reflex as rx


def icon_button(icon: str, url: str, size: int, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon, size=size),
            text,
            variant="solid" if solid else "surface",
        ),
        href=url,
        is_external=True
    )
