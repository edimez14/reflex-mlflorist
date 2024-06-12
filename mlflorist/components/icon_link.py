import reflex as rx


def icon_link(icon: str, url: str, text="",) -> rx.Component:
    return rx.link(
        rx.mobile_only(
            rx.icon(icon, size=15),
            text,
        ),
        rx.tablet_and_desktop(
            rx.icon(icon, size=20),
            text,
        ),
        href=url,
        is_external=True
    )
