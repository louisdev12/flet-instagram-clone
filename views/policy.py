import flet as ft

PRIMARY_COLOR = "#1DA1F2"
TEXT_COLOR = ft.Colors.WHITE70

def policy_view(page: ft.Page):
    page_width = min(page.window.width or 390, 430)
    content_width = page_width - 40

    def styled_text(text, size=15, color=TEXT_COLOR, weight=None):
        return ft.Text(text, size=size, color=color, weight=weight)

    top_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Agree to Instagram's terms and policies",
                    size=24,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.WHITE,
                    overflow=ft.TextOverflow.VISIBLE,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        width=content_width,
        padding=ft.padding.symmetric(horizontal=10),
        margin=ft.margin.only(bottom=20),
    )

    first_paragraph = ft.Row(
        [
            styled_text("People who use our services may have uploaded your contact information to "),
            styled_text("Instagram "),
            styled_text("learn more", color=PRIMARY_COLOR),
        ],
        wrap=True,
        spacing=0,
    )

    agreement_text = ft.Column(
        [
            ft.Row(
                [
                    styled_text("By tapping "),
                    styled_text("I agree", color=ft.Colors.WHITE, weight=ft.FontWeight.W_600),
                    styled_text(", you agree to create an"),
                ],
                wrap=True,
                spacing=0,
            ),
            ft.Row(
                [
                    styled_text("account and to Instagram's "),
                    styled_text("Terms, ", color=PRIMARY_COLOR, weight=ft.FontWeight.W_500),
                    styled_text("Privacy Policy ", color=PRIMARY_COLOR, weight=ft.FontWeight.W_500),
                    styled_text("and "),
                    styled_text("Cookies Policy", color=PRIMARY_COLOR, weight=ft.FontWeight.W_500),
                    styled_text("."),
                ],
                wrap=True,
                spacing=0,
            ),
        ],
        spacing=5,
    )

    privacy_info = ft.Column(
        [
            ft.Row(
                [
                    styled_text("The "),
                    styled_text("Privacy Policy", color=PRIMARY_COLOR, weight=ft.FontWeight.W_500),
                    styled_text(" describes the ways we"),
                ],
                wrap=True,
                spacing=0,
            ),
            styled_text("can use the information we collect when you create an account."),
            ft.Container(height=8),
            styled_text("For example, we use this information to provide, personalise and improve our products, including ads."),
        ],
        spacing=0,
    )

    content_section = ft.Container(
        content=ft.Column(
            [first_paragraph, agreement_text, privacy_info],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20,
        ),
        width=content_width,
        padding=ft.padding.symmetric(horizontal=10),
    )

    agree_button = ft.Container(
        content=styled_text("I agree", color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.W_600),
        bgcolor="#0064E0",
        border_radius=30,
        height=50,
        width=content_width,
        alignment=ft.alignment.center,
        on_click=lambda e: page.go("/add_profile_pic"),
        margin=ft.margin.symmetric(vertical=20),
    )

    scrollable_content = ft.Container(
        content=ft.Column(
            [
                top_section,
                content_section,
                agree_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        ),
        expand=True,
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
    )

    bottom_fixed = ft.Container(
        content=styled_text(
            "I already have an account",
            size=16,
            color=PRIMARY_COLOR,
            weight=ft.FontWeight.W_500,
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.only(bottom=20, top=10),
    )

    app_bar = ft.AppBar(
        leading=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.WHITE,
            on_click=lambda _: page.go("/username"),
        ),
        bgcolor=ft.Colors.TRANSPARENT,
        elevation=0,
        toolbar_height=56,
        leading_width=60,
    )

    return ft.View(
        route="/policy",
        controls=[
            ft.Column(
                [
                    scrollable_content,
                    bottom_fixed  # Always at the bottom
                ],
                expand=True,
                spacing=0,
            )
        ],
        appbar=app_bar,
        bgcolor="#152127",
        padding=ft.padding.all(0),
        spacing=0,
    )
