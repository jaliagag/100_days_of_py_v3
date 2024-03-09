from rxconfig import config
import reflex as rx
from cien_dias.views.navbar import navbar


class State(rx.State):
    """The app state."""

@rx.page(title="100 days of python")
def index() -> rx.Component:
    return rx.container(
        navbar(),
        rx.box(
            "Usando Reflex",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "Si, todo python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


app = rx.App()
app.add_page(index)
