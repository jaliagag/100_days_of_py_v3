import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("100 Dias de Python! junto a @jahumada"),
        ),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu", variant="soft"),
            ),
            rx.menu.content(
                rx.menu.item("Home", shortcut="⌘ E"),
                rx.menu.item("Duplicate", shortcut="⌘ D"),
                rx.menu.separator(),
                rx.menu.item("Archive", shortcut="⌘ N"),
                rx.menu.sub(
                    rx.menu.sub_trigger("More"),
                    rx.menu.sub_content(
                        rx.menu.item("Move to project…"),
                        rx.menu.item("Move to folder…"),
                        rx.menu.separator(),
                        rx.menu.item("Advanced options…"),
                    ),
                ),
                rx.menu.separator(),
                rx.menu.item("Share"),
                rx.menu.item("Add to favorites"),
                rx.menu.separator(),
                rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            ),
        ),
        position="sticky",
        width="100%",
        top="0px",
        z_index="999",
        bg="lightgray"
    )
