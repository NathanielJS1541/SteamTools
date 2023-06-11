from __future__ import annotations

# SteamTools Imports.
from steamtools.tui import dashboard

# Rich Imports.
from rich.markdown import Markdown

# Textual Imports
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static

# -------------------------------------------- Classes --------------------------------------------


class SplashScreen(Container):
    pass


class IntroPopup(Container):
    def compose(self) -> ComposeResult:
        yield Static(Markdown(dashboard.SPLASH_MD))
        yield Button("Go To Dashboard", variant="success")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.add_note("[b magenta]Start!")
        self.app.query_one(".location-first").scroll_visible(duration=0.5, top=True)

# -------------------------------------------------------------------------------------------------
