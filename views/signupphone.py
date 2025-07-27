import flet as ft

def signupphone_view(page: ft.Page):
    # Top section with title and description
    top_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "What's your mobile number?", 
                    size=24, 
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.LEFT,
                ),
                ft.Container(height=15),
                ft.Text(
                    "Enter the mobile number on which you can be contacted. No one will see this on your profile.", 
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
            hint_text='Mobile number',
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
    
    # WhatsApp/SMS notification text
    notification_text = ft.Container(
        content=ft.Text(
            "You may receive WhatsApp and SMS notifications from us for security and login purposes.", 
            size=13,
            color=ft.Colors.WHITE60,
            text_align=ft.TextAlign.LEFT,
        ),
        width=370,
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
        on_click=lambda _: print('Next button clicked!'),
    )
    
    # Sign up with email button
    email_signup_button = ft.Container(
        content=ft.Text(
            "Sign up with email address",
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
        on_click=lambda _: print('Email signup clicked!'),
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
            on_click=lambda _: print('Already have account clicked!'),
        ),
        alignment=ft.alignment.center,
    )
    
    # Main layout with proper spacing
    main_content = ft.Column(
        [
            top_section,           # Title and description
            mobile_input,          # Mobile number input
            notification_text,     # WhatsApp/SMS text
            next_button,           # Next button
            email_signup_button,   # Email signup option
            middle_spacer,         # Flexible spacer
            bottom_section,        # Already have account link
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    return ft.View(
        route="/signupphone",
        controls=[main_content],
        appbar=ft.AppBar(
            toolbar_height=30,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: page.go("/login"),
            ),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0,
        ),
        bgcolor='#152127',
        padding=ft.padding.all(20),
    )