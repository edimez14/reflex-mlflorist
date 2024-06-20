import reflex as rx
from mlflorist.components.icon_link import icon_link
from mlflorist.data import Media
from mlflorist.styles.styles import Size


def media(data: Media, footer=False) -> rx.Component:
    return rx.hstack(
        rx.cond(
            footer == False,
            rx.hstack(
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
            ),
        ),
        rx.cond(
            footer == True,
            rx.hstack(
                icon_link(
                    data.email.icon,
                    data.email.url,
                    True
                ),
                icon_link(
                    data.twitter.icon,
                    data.twitter.url,
                    True
                ),
                icon_link(
                    data.tiktok.icon,
                    data.tiktok.url,
                    True
                ),
                icon_link(
                    data.instagram.icon,
                    data.instagram.url,
                    True
                ),
                icon_link(
                    data.pinterest.icon,
                    data.pinterest.url,
                    True
                ),
                icon_link(
                    data.likedin.icon,
                    data.likedin.url,
                    True
                ),
            ),
        ),
        spacing=Size.SMALL.value
    )
