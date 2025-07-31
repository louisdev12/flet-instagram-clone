import flet as ft

def username_view(page: ft.Page):
    # Top section with title and description
    top_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Create a username ", 
                    size=24, 
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.LEFT,
                ),
                ft.Text(
                    "Add a username or use our suggestion. You can change this at any time ", 
                    size=15, 
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.LEFT,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=0,
        ),
        width=370,
        padding=ft.padding.symmetric(horizontal=5),
    )
    
    # Mobile number input field
    name_input = ft.Container(
        content=ft.TextField(
            hint_text='Username',
            border_radius=15,
            height=55,
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.WHITE,
            hint_style=ft.TextStyle(color=ft.Colors.WHITE60, size=16),
            bgcolor=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.WHITE,
            focused_border_width=1.5,
            border_color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
            content_padding=ft.padding.symmetric(horizontal=20, vertical=15),
            text_style=ft.TextStyle(size=16),
        ),
        padding=ft.padding.symmetric(horizontal=5),
    )
    
    # Next button
    next_button = ft.Container(
        content=ft.Text(
            "Next",
            color=ft.Colors.WHITE,
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
        bgcolor='#0064E0',
        border_radius=25,
        height=55,
        width=370,
        alignment=ft.alignment.center,
        on_click=lambda e: page.go("/policy"),
    )
    
    
    # Middle spacer for flexible spacing
    middle_spacer = ft.Container(
        content=ft.Text(""),
        expand=1,
    )
    
    # Bottom "I already have an account" section
    bottom_section = ft.Container(
        content=ft.TextButton(
            "I already have an account",
            style=ft.ButtonStyle(
                color="#0064E0",
                overlay_color=ft.Colors.TRANSPARENT,
            ),
            on_click=lambda _: page.go("/login"),
        ),
        alignment=ft.alignment.center,
    )

    # Main layout with proper spacing
    main_content = ft.Column(
        [
            top_section,           # Title and description
            name_input,          # Mobile number input
            next_button,           # Next button
            middle_spacer,         # Flexible spacer
            bottom_section,        # Already have account link
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    return ft.View(
        route="/username",
        controls=[main_content],
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/name"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        bgcolor='#152127',
        padding=ft.padding.all(20),
    )