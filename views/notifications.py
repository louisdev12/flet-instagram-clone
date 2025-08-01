import flet as ft

PRIMARY_COLOR = "#1DA1F2"  # Instagram blue
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"  # Pure black background

def turn_on_notifications_view(page: ft.Page):
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

    # Title
    title = styled_text(
        "Turn on notifications",
        size=24,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER
    )

    # Subtitle
    subtitle = styled_text(
        "Find out straight away when people follow you or like and comment on your posts.",
        size=16,
        color=ft.Colors.WHITE70,
        text_align=ft.TextAlign.CENTER
    )

    # Notification icon with gradient background (simplified as colored container)
    notification_icon = ft.Container(
        content=ft.Container(
            content=ft.Icon(
                name=ft.Icons.FAVORITE,
                size=40,
                color=ft.Colors.PINK_400
            ),
            width=80,
            height=80,
            bgcolor=ft.Colors.BLACK,
            border_radius=20,
            alignment=ft.alignment.center,
            border=ft.border.all(2, ft.Colors.PINK_400)
        ),
        width=100,
        height=100,
        bgcolor=ft.Colors.TRANSPARENT,
        border_radius=25,
        alignment=ft.alignment.center,
        # Gradient effect simulation with border
        border=ft.border.all(3, ft.Colors.PINK_400),
        margin=ft.margin.only(bottom=20)
    )

    # Toggle switch container
    toggle_container = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Icon(
                        name=ft.Icons.POWER_SETTINGS_NEW,
                        size=30,
                        color=TEXT_COLOR
                    ),
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.TRANSPARENT,
                    border_radius=25,
                    alignment=ft.alignment.center,
                    border=ft.border.all(2, TEXT_COLOR)
                ),
                ft.Container(
                    content=ft.Switch(
                        value=True,
                        active_color=PRIMARY_COLOR,
                        inactive_thumb_color=ft.Colors.WHITE,
                        inactive_track_color=ft.Colors.GREY_600,
                    ),
                    margin=ft.margin.only(left=20)
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=content_width,
        height=60,
        alignment=ft.alignment.center,
        margin=ft.margin.symmetric(vertical=30)
    )

    # Next Button
    next_btn = ft.Container(
        content=ft.ElevatedButton(
            "Next",
            bgcolor=PRIMARY_COLOR,
            color=ft.Colors.WHITE,
            height=50,
            on_click=lambda e: page.go("/facebook_suggestions"),
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
            ft.Container(height=40),  # Top spacing after back button
            ft.Container(
                content=title,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            ft.Container(height=20),
            ft.Container(
                content=subtitle,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=40)
            ),
            ft.Container(height=80),  # Space before icon
            notification_icon,
            toggle_container,
            ft.Container(expand=True),  # This pushes the button to the bottom
            next_btn,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        expand=True,
    )

    # Main layout with back button at top
    layout = ft.Column(
        [
            ft.Container(
                content=content_layout,
                expand=True
            )
        ],
        spacing=0,
        expand=True,
    )

    return ft.View(
        route="/turn_on_notifications",
        controls=[layout],
        bgcolor=BG_COLOR,
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/allow_contacts"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        padding=ft.padding.all(20),
    )
