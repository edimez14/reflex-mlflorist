import reflex as rx
from mlflorist.components.heading import heading
from mlflorist.components.info_detail import info_detail
from mlflorist.data import Experience
from mlflorist.styles.styles import MAX_WIDTH, Size, EmSize


def info(title: str, info: list[Experience]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.mobile_only(
            rx.vstack(
                info_detail(info.experience_1),
                info_detail(info.experience_2),
                info_detail(info.experience_3),
                spacing=Size.DEFAULT.value,
                width="100%",
                padding_x=EmSize.DEFAULT.value,
                padding_y=EmSize.SMALL.value,
            ),
        ),
        rx.tablet_and_desktop(
            rx.vstack(
                info_detail(info.experience_1),
                info_detail(info.experience_2, True),
                info_detail(info.experience_3),
                max_width=MAX_WIDTH,
                spacing=Size.DEFAULT.value,
                width="100%",
                padding_x=EmSize.DEFAULT.value,
                padding_y=EmSize.SMALL.value,
            ),
        ),
    )