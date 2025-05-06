import reflex as rx


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    fields = [
        "field1"
    ]
    return rx.foreach(
        fields,
        lambda field: rx.upload(
            rx.text(
                "Drag and drop files here or click to select files"
            ),
            id="upload",
        )
    )


app = rx.App()
app.add_page(index)
