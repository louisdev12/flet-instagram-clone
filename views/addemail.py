import flet as ft

PRIMARY_COLOR = "#1DA1F2"  # Instagram blue
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"  # Pure black background

def add_email_view(page: ft.Page):
    page_width = min(page.window.width or 390, 430)
    content_width = page_width - 40

    def styled_text(text, size=16, color=TEXT_COLOR, weight=None, text_align=None):
        return ft.Text(
            text,
            size=size,
            color=color,
            weight=weight,
            text_align=text_align,
        )

    # Top header
    top_row = ft.Row(
        [
            ft.Container(expand=True),  # Spacer
            ft.TextButton(
                "Skip",
                style=ft.ButtonStyle(
                    color=TEXT_COLOR,
                    text_style=ft.TextStyle(
                        size=16,
                        weight=ft.FontWeight.W_400
                    )
                )
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Title
    title = styled_text(
        "Add an email address",
        size=24,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER
    )

    # Subtitle
    subtitle = styled_text(
        "Enter the email address at which you can be contacted. No one will see this on your profile.",
        size=16,
        color=ft.Colors.WHITE70,
        text_align=ft.TextAlign.CENTER
    )

    # Email input field
    email_field = ft.Container(
        content=ft.TextField(
            hint_text="Email address",
            hint_style=ft.TextStyle(color=ft.Colors.WHITE60, size=16),
            text_style=ft.TextStyle(color=TEXT_COLOR, size=16),
            bgcolor=ft.Colors.TRANSPARENT,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.TRANSPARENT,
            cursor_color=TEXT_COLOR,
            border_radius=0,
            content_padding=ft.padding.only(bottom=10),
        ),
        width=content_width,
        margin=ft.margin.only(top=40, bottom=10),
        border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.WHITE60))
    )

    # Meta disclaimer text
    meta_text = styled_text(
        "Meta uses this email address across all of your accounts in Accounts Centre to personalise experiences, such as connecting people and improving ads on our products. Learn more.",
        size=14,
        color=ft.Colors.WHITE60,
        text_align=ft.TextAlign.LEFT
    )

    # Next Button
    next_btn = ft.Container(
        content=ft.ElevatedButton(
            "Next",
            bgcolor=PRIMARY_COLOR,
            color=ft.Colors.WHITE,
            height=50,
            width=content_width,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                text_style=ft.TextStyle(
                    size=16,
                    weight=ft.FontWeight.W_600
                )
            )
        ),
        margin=ft.margin.only(top=40, bottom=40)
    )

    # Main content layout
    content_layout = ft.Column(
        [
            ft.Container(height=40),  # Top spacing after header
            ft.Container(
                content=title,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            ft.Container(height=30),
            ft.Container(
                content=subtitle,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            email_field,
            ft.Container(height=30),
            ft.Container(
                content=meta_text,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            ft.Container(expand=True),  # Flexible space to push button to bottom
            next_btn,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        expand=True,
    )

    # Main layout
    layout = ft.Column(
        [
            ft.Container(
                content=top_row,
                padding=ft.padding.symmetric(horizontal=10, vertical=15)
            ),
            ft.Container(
                content=content_layout,
                expand=True
            )
        ],
        spacing=0,
        expand=True,
    )

    return ft.View(
        route="/add_email",
        controls=[layout],
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/follow_people"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        bgcolor=BG_COLOR,
        padding=ft.padding.all(20),
    )
