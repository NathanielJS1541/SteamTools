from __future__ import annotations

# SteamTools Imports.
from steamtools.tui import dashboard, splashscreen, notification

# Rich imports.
from rich.console import RenderableType
from rich.text import Text

# Textual Imports.
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, TextLog

# Web browser import for opening links.
import webbrowser


class SteamTools(App[None]):
    """
    Main app for the SteamTools TUI. Call .run() to launch the app.
    """

    # Path to the .css file for the application.
    CSS_PATH = "application.css"

    # The title for the application that is displayed in the header.
    TITLE = "SteamTools"

    # Define KeyBindings for the SteamTools app.
    BINDINGS = [
        ("ctrl+b", "toggle_sidebar", "Sidebar"),
        ("ctrl+t", "app.toggle_dark", "Toggle Dark mode"),
        ("ctrl+s", "app.screenshot()", "Screenshot"),
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Debug Console"),
        Binding("ctrl+c,ctrl+q", "app.quit", "Quit", show=True),
    ]

    # By default, the sidebar is hidden. The user must press "ctrl+b" to open it.
    show_sidebar = reactive(False)

    # Define the main layout for the application.
    def compose(self) -> ComposeResult:
        # All elements are contained within a container.
        yield Container(
            # The header is displayed at the top, and contains the title and a clock.
            Header(show_clock=True),
            # The dashboard body contains the main elements of the TUI.
            dashboard.Body(
                # The SplashScreen is displayed when the app is first opened.
                splashscreen.SplashScreen(
                    splashscreen.IntroPopup(), classes="location-splash"
                ),
                # The QuickAccess container is used to easily navigate from screen to screen.
                dashboard.QuickAccess(
                    dashboard.LocationLink("Dashboard", ".location-dashboard")
                ),
                # The changing portion of the TUI is stored in a column.
                dashboard.Column(
                    # This section stores the content for the dashboard.
                    dashboard.Section(
                        # Dashboard Title.
                        dashboard.SectionTitle("Dashboard"),
                        # Display a message explaining how to get an API key.
                        dashboard.Message(dashboard.GET_API_KEY),
                        # Display the API Key Entry Box.
                        dashboard.APIKeyEntry(),
                    ),
                    classes="location-dashboard location-first",
                ),
            ),
            # The Sidebar is part of the hidden class by default.
            dashboard.Sidebar(classes="-hidden"),
            # Textlog watches the hidden classes and displays text in a scrolling panel.
            TextLog(classes="-hidden", wrap=False, highlight=True, markup=True),
        )
        # The footer displays the keybindings and allows a user to enter the keybindings with their mouse.
        yield Footer()

    # Adds text to the TextLog.
    def add_note(self, note: RenderableType) -> None:
        """
        Adds a note to the textlog for the application.
        :param note: Text as a RenderableType to add to the TextLog.
        :return: None
        """
        self.query_one(TextLog).write(note)

    # Define how opening a link within this application should be handled.
    def action_open_link(self, link: str) -> None:
        # Play a bell sound.
        self.app.bell()
        # Open the link in the default browser.
        webbrowser.open(link)

    # Define how the sidebar is toggled between visible and invisible.
    def action_toggle_sidebar(self) -> None:
        sidebar = self.query_one(dashboard.Sidebar)
        # Remove focus from anything that may have it.
        self.set_focus(None)
        # Remove the sidebar from the hidden class if it is part of it.
        if sidebar.has_class("-hidden"):
            sidebar.remove_class("-hidden")
        # Otherwise, un-focus the screen from the widget and add it to the hidden class.
        else:
            if sidebar.query("*:focus"):
                self.screen.set_focus(None)
            sidebar.add_class("-hidden")

    def on_mount(self) -> None:
        self.add_note("SteamTools Dashboard app is running.")
        self.query_one("SplashScreen Button", Button).focus()

    # Define how a screenshot should be taken of the application.
    def action_screenshot(self, filename: str | None = None, path: str = "./") -> None:
        """
        Save an SVG "screenshot". This action will save an SVG file containing the current contents of the screen.

        :param filename: Filename of screenshot, or None to auto-generate.
        :param path: Path to directory.
        :return: None
        """
        # Play a bell sound.
        self.bell()
        # Save a screenshot of the current app.
        path = self.save_screenshot(filename, path)
        # Create a message explaining where the screenshot was saved to.
        message = Text.assemble("Screenshot saved to ", (f"'{path}'", "bold green"))
        # Add the message to the TextLog.
        self.add_note(message)
        # Display the message in a PopUp notification.
        self.screen.mount(notification.PopUp(message))
