import flet as ft

PRIMARY_COLOR = "#0064E0"
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#152127"  # background color similar to image

def add_profile_pic_view(page: ft.Page):
    page_width = min(page.window.width or 390, 430)
    content_width = page_width - 40

    def styled_text(text, size=16, color=TEXT_COLOR, weight=None):
        return ft.Text(
            text,
            size=size,
            color=color,
            weight=weight,
            text_align="center"
        )

    # Title and Subtitle
    title = styled_text(
        "Add a profile picture",
        size=22,
        weight=ft.FontWeight.W_600
    )
    subtitle = styled_text(
        "Add a profile picture so that your friends know it's you. "
        "Everyone will be able to see your picture.",
        size=14,
        color=ft.Colors.WHITE70
    )

    # Avatar Placeholder
    avatar = ft.CircleAvatar(
        radius=60,
        content=ft.Icon(
            name=ft.Icons.PERSON,
            size=80,
            color=ft.Colors.WHITE
        ),
        bgcolor="#2D3338"
    )

    # Buttons
    add_pic_btn = ft.Container(
        content=ft.ElevatedButton(
            "Add picture",
            bgcolor=PRIMARY_COLOR,
            color=ft.Colors.WHITE,
            height=45,
            width=content_width,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=30)
            )
        ),
        margin=ft.margin.only(bottom=10)
    )

    skip_btn = ft.Container(
        content=ft.OutlinedButton(
            "Skip",
            height=45,
            width=content_width,
            on_click=lambda e: page.go("/allow_contacts"),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=30),
                side=ft.BorderSide(1, ft.Colors.WHITE70)
            )
        )
    )

    # Layout
    layout = ft.Column(
        [
            ft.Container(height=40),
            title,
            ft.Container(height=10),
            subtitle,
            ft.Container(height=40),
            avatar,
            ft.Container(expand=True),
            add_pic_btn,
            skip_btn,
            ft.Container(height=20),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.START,
        spacing=0,
        expand=True,
    )

    return ft.View(
        route="/add_profile_pic",
        controls=[layout],
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/policy"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        bgcolor=BG_COLOR,
        padding=ft.padding.all(20),
    )
