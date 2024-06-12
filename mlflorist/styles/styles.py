from enum import Enum
import reflex as rx

MAX_WIDTH = "1200px"
IMAGE_HEIGHT = "200px"
AVATAR_HEIGHT = "300px"

class EmSize(Enum):
    ZERO = "0em"
    SMALL = "0.5em" 
    DEFAULT = "1em"  # 16px
    SMEDIUM = "1.5em"
    MEDIUM = "2em"
    BIG = "4em"
    XBIG = "6em"


class Size(Enum):
    ZERO = "0"
    SXSMALL = "1"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px
    XBIG = "9"

class Colors(Enum):
    aliceblue = "#F0F8FF"
    oldlace = "#FDF5E6"
    black = "#000000"
    floralwhite = "#FFFAF0"
    hotpink = "#FF69B4"
    aqua = "#00FFFF"
    ivory = "#FFFFF0"


glassmorphism = dict(
    background_color="rgba(225, 225, 225, 0.25)",
    box_shadow="0 8px 32px 0 rgba(0, 0, 0, 0.37)",
    backdrop_filter="blur(0.1px)",
    border="2px solid rgba(225, 225, 225, 0.15)",
    border_radius="20px"
)
    

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}