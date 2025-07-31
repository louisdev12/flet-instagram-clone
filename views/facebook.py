import flet as ft

PRIMARY_COLOR = "#1DA1F2"  # Instagram blue
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"  # Pure black background

def facebook_suggestions_view(page: ft.Page):
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

    # Top row with back button and skip
    top_row = ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=TEXT_COLOR,
                icon_size=24,
            ),
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
        expand=False
    )

    # Title
    title = styled_text(
        "Get Facebook suggestions",
        size=24,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER
    )

    # Subtitle
    subtitle = styled_text(
        "You can find people you know from Facebook with Accounts Centre.",
        size=16,
        color=ft.Colors.WHITE70,
        text_align=ft.TextAlign.CENTER
    )

    # Phone with Facebook icon and connecting dots
    phone_facebook_icon = ft.Container(
        content=ft.Stack(
            [
                # Phone outline
                ft.Container(
                    content=ft.Icon(
                        name=ft.Icons.SMARTPHONE,
                        size=80,
                        color=TEXT_COLOR
                    ),
                    width=120,
                    height=120,
                    alignment=ft.alignment.center,
                ),
                # Facebook icon in the center
                ft.Container(
                    content=ft.Container(
                        content=ft.Text(
                            "f",
                            size=24,
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
                        ),
                        width=40,
                        height=40,
                        bgcolor="#1877F2",  # Facebook blue
                        border_radius=20,
                        alignment=ft.alignment.center,
                    ),
                    left=40,
                    top=40,
                ),
                # Left connecting dot (Instagram colors)
                ft.Container(
                    content=ft.Container(
                        width=20,
                        height=20,
                        bgcolor=ft.Colors.TRANSPARENT,
                        border_radius=10,
                        border=ft.border.all(2, ft.Colors.PINK_400),
                    ),
                    left=-10,
                    top=50,
                ),
                # Right connecting dot (Instagram colors)
                ft.Container(
                    content=ft.Container(
                        width=20,
                        height=20,
                        bgcolor=ft.Colors.TRANSPARENT,
                        border_radius=10,
                        border=ft.border.all(2, ft.Colors.PURPLE_400),
                    ),
                    right=-10,
                    top=50,
                ),
                # Connecting lines (simplified as small containers)
                ft.Container(
                    content=ft.Container(
                        width=30,
                        height=2,
                        bgcolor=ft.Colors.PINK_400,
                    ),
                    left=10,
                    top=59,
                ),
                ft.Container(
                    content=ft.Container(
                        width=30,
                        height=2,
                        bgcolor=ft.Colors.PURPLE_400,
                    ),
                    right=10,
                    top=59,
                ),
            ],
            width=120,
            height=120,
        ),
        alignment=ft.alignment.center,
        margin=ft.margin.symmetric(vertical=40)
    )

    # Continue Button
    continue_btn = ft.Container(
        content=ft.ElevatedButton(
            "Continue",
            bgcolor=PRIMARY_COLOR,
            color=ft.Colors.WHITE,
            on_click=lambda e: page.go("/follow_people"),
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
            ft.Container(height=20),
            ft.Container(
                content=subtitle,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=40)
            ),
            ft.Container(height=60),  # Space before icon
            phone_facebook_icon,
            ft.Container(expand=True),  # Flexible space to push button to bottom
            continue_btn,
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
                padding=ft.padding.symmetric(horizontal=10, vertical=10)
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
        route="/facebook_suggestions",
        controls=[layout],
        bgcolor=BG_COLOR,
        padding=ft.padding.all(20),
    )
