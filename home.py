from textual.app import App, ComposeResult, RenderResult
from textual import events
from textual.widget import Widget
import subprocess


class CardHeader(Widget):
    def render(self) -> RenderResult:
        return "Welcome to my home"


class CardItems(Widget):
    def render(self) -> RenderResult:
        return "f: fastfetch\nn: nvim\nq: quit"


class Home(App[None]):
    CSS_PATH = "globals.tcss"

    def compose(self) -> ComposeResult:
        yield CardHeader()
        yield CardItems()

    # Events
    def on_key(self, event: events.Key) -> None:
        if event.key == "f":
            subprocess.run(["fastfetch"], shell=True)
        if event.key == "n":
            subprocess.run(["nvim"], shell=True)
        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = Home()
    app.run()
