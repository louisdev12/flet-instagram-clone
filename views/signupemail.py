import flet as ft

def signupemail_view(page: ft.Page):
    # Top section with title and description
    top_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "What's your email address?", 
                    size=24, 
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.LEFT,
                ),
                ft.Container(height=15),
                ft.Text(
                    "Enter the email address at which you can be contacted. No one will see this on your profile.", 
                    size=15,
                    color=ft.Colors.WHITE70,
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
    mobile_input = ft.Container(
        content=ft.TextField(
            hint_text='Email address',
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
    # Function to handle bottom sheet opening
    def open_bottom_sheet(e):
        page.open(bs)
    
    # Function to handle login navigation
    def handle_login(e):
        page.close(bs)
        page.go("/login")
    
    # Function to handle email verification navigation
    def handle_create_account(e):
        page.close(bs)
        page.go("/emailverification")
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
        on_click=open_bottom_sheet,
    )
    # Existing account button (using ElevatedButton for better reliability)
    existing_account_button = ft.ElevatedButton(
        content=ft.Text(
            "Log in to an existing account",
            color=ft.Colors.WHITE,
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
        style=ft.ButtonStyle(
            bgcolor='#0064E0',
            shape=ft.RoundedRectangleBorder(radius=25),
            elevation=0,
            overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
        ),
        height=55,
        width=370,
        on_click=handle_login,
    )
    create_account_button = ft.ElevatedButton(
        content=ft.Text(
            "Create new account",
            color=ft.Colors.WHITE,
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.TRANSPARENT,
            side=ft.BorderSide(1.5, ft.Colors.with_opacity(0.4, ft.Colors.WHITE)),
            shape=ft.RoundedRectangleBorder(radius=25),
            elevation=0,
            overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
        ),
        height=55,
        width=370,
        on_click=handle_create_account,
    )
    # Bottom sheet with proper button implementations
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Are you trying to log in?", size=22, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "This email is associated with an existing account. You can log in to it or create a new account with a new password.", 
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Column([
                        existing_account_button,
                        create_account_button,
                        ft.Container(height=50)
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            ),
            padding=ft.padding.only(top=10, left=10, right=10, bottom=100),
            expand=True
        ),
        open=False,
        dismissible=True,
        show_drag_handle=True,
        enable_drag=True,
    )
    # Sign up with email button
    phone_signup_button = ft.Container(
        content=ft.Text(
            "Sign up with Mobile Number",
            color=ft.Colors.WHITE,
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
        bgcolor=ft.Colors.TRANSPARENT,
        border=ft.border.all(1.5, ft.Colors.with_opacity(0.4, ft.Colors.WHITE)),
        border_radius=25,
        height=55,
        width=370,
        alignment=ft.alignment.center,
        on_click=lambda _: page.go("/signupphone"),
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
            mobile_input,          # Mobile number input
            next_button,           # Next button
            phone_signup_button,   # Email signup option
            middle_spacer,         # Flexible spacer
            bottom_section,        # Already have account link
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    return ft.View(
        route="/signupemail",
        controls=[main_content],
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/signupphone"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        bgcolor='#152127',
        padding=ft.padding.all(20),
    )