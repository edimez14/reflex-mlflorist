import reflex as rx

def boxicon(icon_class: str, size: str) -> rx.Component:
    return rx.html(f'<i class="{icon_class}" style="font-size: {size};"></i>')