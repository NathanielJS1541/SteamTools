from __future__ import annotations

# Textual imports
from textual.widgets import Static

# ------------------------------------------- Constants -------------------------------------------

POPUP_DURATION = 3

# -------------------------------------------------------------------------------------------------

# -------------------------------------------- Classes --------------------------------------------


class PopUp(Static):
    """
    Defines a PopUp notification based on the Static class.

    Displays for 3 seconds.
    """
    def on_mount(self) -> None:
        self.set_timer(POPUP_DURATION, self.remove)

    def on_click(self) -> None:
        self.remove()

# -------------------------------------------------------------------------------------------------
