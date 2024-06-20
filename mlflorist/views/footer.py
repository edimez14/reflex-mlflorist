import reflex as rx
from mlflorist.components.media import media
from mlflorist import data
from mlflorist.data import Footer
from mlflorist.styles.styles import EmSize, Size, glassmorphism
from mlflorist.components.media import media

DATA = data.data

def footer(data_footer: Footer) -> rx.Component:
    return rx.vstack(
        rx.mobile_only(
            rx.vstack(
                rx.vstack(
                    rx.vstack(
                        data_footer.description,
                        rx.button(data_footer.button_whatsapp),
                        spacing=Size.SMALL.value,
                        # align="center",
                        width="100%",
                    ),
                    rx.divider(bg="black"),
                    rx.vstack(
                        data_footer.title,
                        media(DATA.media, True),
                        align="center",
                        width="100%",
                    ),
                    padding_x=EmSize.BIG.value,
                    padding_y=EmSize.DEFAULT.value,
                    width="100%",
                ),
            ),
        ),
        rx.tablet_and_desktop(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        data_footer.description,
                        rx.button(data_footer.button_whatsapp),
                        spacing=Size.SMALL.value,
                        # align="center",
                        width="50%",
                    ),
                    rx.divider(orientation="vertical", bg="black"),
                    rx.vstack(
                        data_footer.title,
                        media(DATA.media, True),
                        align="center",
                        width="50%",
                    ),
                    padding_x=EmSize.BIG.value,
                    padding_y=EmSize.DEFAULT.value,
                    width="100%",
                ),
            ),
        ),
        data_footer.copyright,
        width="100%",
        spacing=Size.SMALL.value,
        padding_x=EmSize.BIG.value,
        padding_y=EmSize.DEFAULT.value,
        style=glassmorphism,
        align="center",
    )
