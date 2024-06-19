import reflex as rx
from mlflorist.data import ExperienceItem
from mlflorist.components.text import texts
from mlflorist.styles.styles import Colors, IMAGE_HEIGHT, IMAGE_WIDTH, EmSize, Size, glassmorphism


def info_detail(info: ExperienceItem, reverse=False) -> rx.Component:
    return rx.box(
        rx.mobile_only(
            rx.box(
                rx.cond(
                    reverse == False,
                    rx.vstack(
                        rx.image(
                            src="/img/bg_header_5.jpeg",
                            width=IMAGE_WIDTH, height=IMAGE_HEIGHT,
                            border_radius="15px 15px",
                            margin="auto",
                        ),
                        rx.vstack(
                            rx.text.strong(info.title),
                            rx.text(info.subtitle),
                            texts(
                                info.description,
                                Size.SMALL.value,
                                Colors.gray.value
                            ),
                            style=glassmorphism,
                            width="100%",
                            padding_x=EmSize.DEFAULT.value,
                            padding_y=EmSize.BIG.value,
                            margin="auto 0",
                        ),
                        # width="100%",
                        spacing=Size.SMALL.value,
                        margin="auto",

                    ),
                ),
            ),
        ),
        rx.tablet_and_desktop(
            rx.box(
                rx.cond(
                    reverse == False,
                    rx.hstack(
                        rx.vstack(
                            rx.text.strong(info.title),
                            rx.text(info.subtitle),
                            texts(
                                info.description,
                                Size.SMALL.value,
                                Colors.gray.value
                            ),
                            style=glassmorphism,
                            width="100%",
                            padding_x=EmSize.DEFAULT.value,
                            padding_y=EmSize.BIG.value,
                            margin="auto 2.5em",
                        ),
                        rx.image(
                            src="/img/bg_header_5.jpeg",
                            width=IMAGE_WIDTH, height=IMAGE_HEIGHT,
                            border_radius="15px 15px",
                        ),
                        # width="100%",
                        spacing=Size.SMALL.value,
                        margin="auto",
                    ),
                ),
            ),
            rx.box(
                rx.cond(
                    reverse == True,
                    rx.hstack(
                        rx.image(
                            src="/img/bg_header_5.jpeg",
                            width=IMAGE_WIDTH, height=IMAGE_HEIGHT,
                            border_radius="15px 15px",
                        ),
                        rx.vstack(
                            rx.text.strong(info.title),
                            rx.text(info.subtitle),
                            texts(
                                info.description,
                                Size.SMALL.value,
                                Colors.gray.value
                            ),
                            style=glassmorphism,
                            width="100%",
                            padding_x=EmSize.DEFAULT.value,
                            padding_y=EmSize.BIG.value,
                            margin="auto 2.5em",
                        ),
                        # width="100%",
                        spacing=Size.SMALL.value,
                        margin="auto",
                    ),
                ),
            ),
        ),
    )