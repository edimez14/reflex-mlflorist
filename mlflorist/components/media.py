import reflex as rx
from mlflorist.components.icon_link import icon_link
from mlflorist.data import Media
from mlflorist.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.hstack(
        icon_link(
            data.email.icon,
            data.email.url,
        ),
        icon_link(
            data.twitter.icon,
            data.twitter.url,
        ),
        icon_link(
            data.tiktok.icon,
            data.tiktok.url,
        ),
        icon_link(
            data.instagram.icon,
            data.instagram.url,
        ),
        icon_link(
            data.pinterest.icon,
            data.pinterest.url,
        ),
        icon_link(
            data.likedin.icon,
            data.likedin.url,
        ),
        spacing=Size.SMALL.value
    )