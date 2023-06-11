from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, HorizontalScroll, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Header, Footer, Label, Input, Button, Static
import webbrowser

# Constant Strings
DASHBOARD_TITLE = "SteamTools Dashboard"
STEAM_API_EXPLANATION = """This app relies on having a Steam API key to access data from Steam.
You can get one from [@click="app.open_link('https://steamcommunity.com/dev/apikey')"]https://steamcommunity.com/dev/apikey[/]
Paste it here and click "Test Key" to check if the API key is valid."""
STEAM_API_TEST_BUTTON = "Test Key"


# Dashboard which will be used as the main landing page for the tui.
class Dashboard(App):
    # External CSS file for the textual dashboard.
    CSS_PATH = "dashboard.css"

    # Set the title for the dashboard, which will be displayed on the header.
    TITLE = DASHBOARD_TITLE

    # The screen is defined as a vertical layout in dashboard.css.
    def compose(self) -> ComposeResult:
        # Header at the top of the dashboard.
        yield Header(show_clock=True)

        # Horizontal group to display the label, input and button all on the same row.
        yield Horizontal(
            Label(STEAM_API_EXPLANATION, id="api-howto-label"),      # Label to explain how to get a Steam API key.
            Input(placeholder="Steam API Key", id="api-key-input"),  # Input box for pasting the API key.
            Static(classes="horizontal-spacer"),                     # Spacer for the button.
            Button(STEAM_API_TEST_BUTTON, id="api-test-button"),     # Button to test whether the API key is valid.
            Static(classes="horizontal-spacer"),                     # Spacer for the button.
        )

    # Action defining how clicking on a web URL should be handled
    def action_open_link(self, link: str) -> None:
        self.app.bell()        # Play the bell sound
        webbrowser.open(link)  # Open the link in the default browser
