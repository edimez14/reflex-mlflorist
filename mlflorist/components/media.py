import reflex as rx
from mlflorist.components.icon_link import icon_link
from mlflorist.data import Media
from mlflorist.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.hstack(
        icon_link(
            "mail",
            data.email,
        ),
        icon_link(
            "twitter",
            data.twitter,
        ),
        icon_link(
            "file-video",
            data.tiktok,
        ),
        icon_link(
            "instagram",
            data.instagram,
        ),
        icon_link(
            "image",
            data.pinterest,
        ),
        icon_link(
            "linkedin",
            data.likedin,
        ),
        spacing=Size.SMALL.value
    )
