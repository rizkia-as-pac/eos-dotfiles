from typing import Final
import os

MOD: Final[str] = "mod4"
ALTERKEY: Final[str] = "mod1"
HOME = os.path.expanduser("~")
TERMINAL: Final[str] = f"{HOME}/.config/qtile/urxvtc.sh"
SECONDARY_TERMINAL: Final[str] = "xterm"


# colors = [
#     ["#282c34", "#282c34"],  # panel background
#     ["#3d3f4b", "#434758"],  # background for current screen tab
#     ["#ffffff", "#ffffff"],  # font color for group names
#     ["#ff5555", "#ff5555"],  # border line color for current tab
#     [
#         "#74438f",
#         "#74438f",
#     ],  # border line color for 'other tabs' and color for 'odd widgets'
#     ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
#     ["#e1acff", "#e1acff"],  # window name
#     ["#ecbbfb", "#ecbbfb"],  # backbround for inactive screens
# ]
