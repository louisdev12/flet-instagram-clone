import flet as ft

PRIMARY_COLOR = "#1DA1F2"  # Instagram blue
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"  # Pure black background like in image

def allow_contacts_view(page: ft.Page):
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

    # Title - centered and wrapped properly
    title = styled_text(
        "Next, you can allow access to your contacts to make it easier to find your friends on Instagram",
        size=24,
        weight=ft.FontWeight.W_500,
        text_align=ft.TextAlign.CENTER
    )

    # Bullet Points with refresh and settings icons
    bullet_point_1 = ft.Row(
        [
            ft.Container(
                content=ft.Icon(
                    name=ft.Icons.REFRESH,
                    size=24,
                    color=TEXT_COLOR
                ),
                margin=ft.margin.only(right=15, top=5)
            ),
            ft.Container(
                content=styled_text(
                    "Your contacts will be periodically synced and stored securely on our servers so that we can help recommend people and things that are relevant to you.",
                    size=16,
                    color=TEXT_COLOR,
                ),
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=0
    )

    bullet_point_2 = ft.Row(
        [
            ft.Container(
                content=ft.Icon(
                    name=ft.Icons.SETTINGS,
                    size=24,
                    color=TEXT_COLOR
                ),
                margin=ft.margin.only(right=15, top=5)
            ),
            ft.Container(
                content=ft.Column(
                    [
                        styled_text(
                            "You can turn off syncing at any time in Settings.",
                            size=16,
                            color=TEXT_COLOR,
                        ),
                        styled_text(
                            "Learn more.",
                            size=16,
                            color=TEXT_COLOR,
                        )
                    ],
                    spacing=5,
                    tight=True
                ),
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=0
    )

    bullet_points = ft.Column(
        [
            bullet_point_1,
            bullet_point_2
        ],
        spacing=30
    )

    # Next Button
    next_btn = ft.Container(
        content=ft.ElevatedButton(
            "Next",
            bgcolor=PRIMARY_COLOR,
            color=ft.Colors.WHITE,
            height=50,
            on_click=lambda e: page.go("/turn_on_notifications"),
            width=content_width,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                text_style=ft.TextStyle(
                    size=16,
                    weight=ft.FontWeight.W_600
                )
            )
        ),
        margin=ft.margin.only(top=40, bottom=20)
    )

    # Bottom disclaimer text
    disclaimer = ft.Container(
        content=styled_text(
            "By tapping Next, you can choose to sync your contacts or skip this step.",
            size=13,
            color=ft.Colors.WHITE60,
            text_align=ft.TextAlign.CENTER
        ),
        width=content_width
    )

    # Main layout with proper spacing
    layout = ft.Column(
        [
            ft.Container(height=60),  # Top spacing
            ft.Container(
                content=title,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            ft.Container(height=60),  # Space between title and bullet points
            ft.Container(
                content=bullet_points,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            ft.Container(expand=True),  # Flexible space to push button to bottom
            next_btn,
            disclaimer,
            ft.Container(height=40),  # Bottom spacing
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        expand=True,
    )

    return ft.View(
        route="/allow_contacts",
        controls=[layout],
        bgcolor=BG_COLOR,
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/add_profile_pic"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        padding=ft.padding.all(20),
    )

