import flet as ft

PRIMARY_COLOR = "#1DA1F2"  # Instagram blue
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"  # Pure black background
SEARCH_BG = "#1C1C1E"  # Dark gray for search bar

def follow_people_view(page: ft.Page):
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

    # Dummy user data
    users = [
        {"name": "Tesla Motors", "username": "teslamotors", "verified": True, "following": True},
        {"name": "Elon Musk", "username": "elonmusk", "verified": True, "following": True},
        {"name": "BMW Group", "username": "bmwglobal", "verified": True, "following": True},
        {"name": "GitHub", "username": "github", "verified": True, "following": True},
        {"name": "Mercedes-Benz", "username": "mercedesbenz", "verified": True, "following": True},
        {"name": "Toyota Global", "username": "toyotaglobal", "verified": True, "following": False},
        {"name": "NVIDIA AI", "username": "nvidia", "verified": True, "following": False},
        {"name": "Porsche", "username": "porsche", "verified": True, "following": False},
        {"name": "Ford Motor Company", "username": "ford", "verified": True, "following": False},
        {"name": "SpaceX", "username": "spacex", "verified": True, "following": False},
    ]

    # Subtitle
    subtitle = styled_text(
        "Following isn't required, but is recommended for a personalized experience.",
        size=14,
        color=ft.Colors.WHITE60,
        text_align=ft.TextAlign.CENTER
    )

    # Search bar
    search_bar = ft.Container(
        content=ft.TextField(
            hint_text="Search",
            hint_style=ft.TextStyle(color=ft.Colors.WHITE60, size=16),
            text_style=ft.TextStyle(color=TEXT_COLOR, size=16),
            bgcolor=SEARCH_BG,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.TRANSPARENT,
            cursor_color=TEXT_COLOR,
            prefix_icon=ft.Icons.SEARCH,
            border_radius=10,
            content_padding=ft.padding.symmetric(horizontal=15, vertical=12)
        ),
        width=content_width,
        margin=ft.margin.symmetric(vertical=15)
    )

    # Create user list items
    def create_user_item(user_data):
        # Generate a simple colored circle as avatar placeholder
        colors = [ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PINK_400, 
                 ft.Colors.PURPLE_400, ft.Colors.ORANGE_400, ft.Colors.RED_400,
                 ft.Colors.TEAL_400, ft.Colors.YELLOW_400]
        avatar_color = colors[hash(user_data["username"]) % len(colors)]
        
        avatar = ft.Container(
            content=ft.Text(
                user_data["name"][0].upper(),
                size=20,
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.BOLD
            ),
            width=50,
            height=50,
            bgcolor=avatar_color,
            border_radius=25,
            alignment=ft.alignment.center
        )

        # User info
        user_info = ft.Column(
            [
                ft.Row(
                    [
                        styled_text(
                            user_data["name"],
                            size=16,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Icon(
                            name=ft.Icons.VERIFIED,
                            size=16,
                            color=PRIMARY_COLOR
                        ) if user_data["verified"] else ft.Container(),
                    ],
                    spacing=5,
                    tight=True
                ),
                styled_text(
                    user_data["username"],
                    size=14,
                    color=ft.Colors.WHITE60
                )
            ],
            spacing=2,
            tight=True
        )

        # Follow button
        follow_button = ft.Container(
            content=ft.Icon(
                name=ft.Icons.CHECK_CIRCLE if user_data["following"] else ft.Icons.RADIO_BUTTON_UNCHECKED,
                size=24,
                color=PRIMARY_COLOR if user_data["following"] else ft.Colors.WHITE60
            ),
            width=30,
            height=30,
            alignment=ft.alignment.center
        )

        return ft.Container(
            content=ft.Row(
                [
                    avatar,
                    ft.Container(
                        content=user_info,
                        expand=True,
                        margin=ft.margin.symmetric(horizontal=15)
                    ),
                    follow_button
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.padding.symmetric(vertical=8, horizontal=5),
            margin=ft.margin.symmetric(vertical=2)
        )

    # User list
    user_list = ft.Column(
        [create_user_item(user) for user in users],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    # Follow button
    follow_btn = ft.Container(
        content=ft.ElevatedButton(
            "Follow",
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
        margin=ft.margin.only(top=20, bottom=10)
    )

    # Main content
    content = ft.Column(
        [
            ft.Container(height=10),
            ft.Container(
                content=subtitle,
                width=content_width,
                padding=ft.padding.symmetric(horizontal=20)
            ),
            search_bar,
            ft.Container(
                content=user_list,
                expand=True
            ),
            follow_btn,
        ],
        spacing=0,
        expand=True,
    )

    # Main layout
    layout = ft.Column(
        [
            ft.Container(
                content=content,
                expand=True
            )
        ],
        spacing=0,
        expand=True,
    )

    return ft.View(
        route="/follow_people",
        controls=[layout],
        bgcolor=BG_COLOR,
        appbar=ft.AppBar(
            toolbar_height=30,
            title=(ft.Row([ft.Text("Try following 5+ people",size=17,weight=ft.FontWeight.W_600),ft.TextButton(
                "Skip",
                on_click=lambda _: page.go("/add_email"),
                style=ft.ButtonStyle(
                    color=TEXT_COLOR,
                    text_style=ft.TextStyle(
                        size=16,
                        weight=ft.FontWeight.W_400
                    )
                )
            )],alignment=ft.MainAxisAlignment.CENTER)),
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/facebook_suggestions"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        padding=ft.padding.all(20),
    )
