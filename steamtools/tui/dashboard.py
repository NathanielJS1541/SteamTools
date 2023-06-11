from __future__ import annotations

# Used to get the current version of the module.
from importlib_metadata import version

# Rich Imports.
from rich.console import RenderableType

# Textual Imports.
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.widgets import Button, Input, Static, Switch

# ---------------------------------------- Static Strings -----------------------------------------

# MarkDown text displayed on the button in the splash screen.
SPLASH_MD = """
# **Welcome to the SteamTools TUI!**

SteamTools should provide a variety of useful tools for interacting with Steam from the command line.
"""

# Information about SteamTools displayed in the sidebar.
STEAMTOOLS_ABOUT = """
[@click="app.open_link('https://github.com/NathanielJS1541/SteamTools')"]SteamTools GitHub Repository[/]

Contributors:
[@click="app.open_link('https://github.com/NathanielJS1541')"]NathanielJS1541[/]
[@click="app.open_link('https://github.com/dominicmason555')"]dominicmason555[/]

This was built using textual and rich. See their GitHub Repositories here.
[@click="app.open_link('https://github.com/Textualize/textual')"]Textual GitHub Repository[/]
[@click="app.open_link('https://github.com/Textualize/rich')"]Rich GitHub Repository[/]
"""

# Information about how to get a Steam API Key displayed by the API Key Entry.
GET_API_KEY = """
This app relies on having a Steam API key to access data from Steam.
You can get one from [@click="app.open_link('https://steamcommunity.com/dev/apikey')"]https://steamcommunity.com/dev/apikey[/]
Paste it here and click "Test Key" to check if the API key is valid.
"""

# -------------------------------------------------------------------------------------------------


class Body(ScrollableContainer):
    pass


class Title(Static):
    pass


class DarkSwitch(Horizontal):
    def compose(self) -> ComposeResult:
        yield Switch(value=self.app.dark)
        yield Static("Toggle Dark Mode", classes="label")

    def on_mount(self) -> None:
        self.watch(self.app, "dark", self.on_dark_change, init=False)

    def on_dark_change(self) -> None:
        self.query_one(Switch).value = self.app.dark

    def on_switch_changed(self, event: Switch.Changed) -> None:
        self.app.dark = event.value


class OptionGroup(Container):
    pass


class SectionTitle(Static):
    pass


class Message(Static):
    pass


class Version(Static):
    def render(self) -> RenderableType:
        return f"[b]v{version('SteamTools')}"


class Sidebar(Container):
    def compose(self) -> ComposeResult:
        yield Title("About SteamTools")
        yield OptionGroup(Message(STEAMTOOLS_ABOUT), Version())
        yield DarkSwitch()


class Section(Container):
    pass


class Column(Container):
    pass


class QuickAccess(Container):
    pass


class LocationLink(Static):
    def __init__(self, label: str, reveal: str) -> None:
        super().__init__(label)
        self.reveal = reveal

    def on_click(self) -> None:
        self.app.query_one(self.reveal).scroll_visible(top=True, duration=0.5)
        self.app.add_note(f"Scrolling to [b]{self.reveal}[/b]")


class APIKeyEntry(Container):
    def compose(self) -> ComposeResult:
        yield Static("Steam API Key", classes="label")
        yield Input(placeholder="Paste your Steam API Key Here!")
        yield Static()
        yield Button("Test API Key", variant="primary")
