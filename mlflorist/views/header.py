import reflex as rx
from mlflorist.components.heading import heading
# from mlflorist.components.media import media
from mlflorist.components.text import texts
from mlflorist.data import Header
from mlflorist.styles.styles import Colors, EmSize, Size


def header(data: Header) -> rx.Component:
    return rx.box(
        rx.mobile_only(
            rx.center(
                rx.vstack(
                    heading(data.title, Colors.ivory.value),
                    texts(data.about, Size.DEFAULT.value, Colors.ivory.value),
                    width="50%",
                    align="center",
                    spacing=Size.MEDIUM.value,
                ),
                width="100%",
                spacing=Size.XBIG.value,
                padding_x=EmSize.DEFAULT.value,
                padding_y=EmSize.XBIG.value,
            ),
        ),
        rx.tablet_and_desktop(
            rx.center(
                rx.vstack(
                    heading(data.title, Colors.ivory.value, True),
                    texts(data.about, Size.MEDIUM.value, Colors.ivory.value),
                    width="50%",
                    align="center",
                    spacing=Size.MEDIUM.value,
                ),
                width="100%",
                spacing=Size.XBIG.value,
                padding_x=EmSize.DEFAULT.value,
                padding_y=EmSize.XBIG.value,
            ),
        ),
        width="100%",
        height="500px",
        border_bottom_left_radius="10px",
        border_bottom_right_radius="10px",
        background_image=f"url('{data.image}')",
        background_size="cover",
        background_position="center"
    )