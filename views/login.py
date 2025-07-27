import flet as ft

def login_view(page: ft.Page):
    # Top spacer container
    top_spacer = ft.Container(
        content=ft.Text(""),  # Empty content for spacing
        expand=1,
    )
    
    # Instagram logo container
    insta_logo_container = ft.Container(
        content=ft.Image(
            src="https://i.imgur.com/s3WlxzH.png",
            width=70,
            height=70,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center,
    )
    
    # Middle spacer container (between logo and inputs)
    middle_spacer = ft.Container(
        content=ft.Text(""),  # Empty content for spacing
        expand=1,
    )
    
    # Input fields and login section
    login_section = ft.Container(
        content=ft.Column(
            [
                # Username/email field
                ft.TextField(
                    hint_text='Username, email address or mobile number',
                    border_radius=10,
                    height=55,
                    color=ft.Colors.WHITE,
                    cursor_color=ft.Colors.WHITE,
                    hint_style=ft.TextStyle(color=ft.Colors.WHITE60, size=15),
                    bgcolor=ft.Colors.TRANSPARENT,
                    focused_border_color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
                    focused_border_width=1.4,
                    border_color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                    content_padding=ft.padding.symmetric(horizontal=10, vertical=15),
                    text_style=ft.TextStyle(size=16),
                ),
                
                ft.Container(height=15),  # Spacing between fields
                
                # Password field
                ft.TextField(
                    hint_text='Password',
                    border_radius=10,
                    height=55,
                    password=True,
                    can_reveal_password=True,
                    color=ft.Colors.WHITE,
                    cursor_color=ft.Colors.WHITE,
                    hint_style=ft.TextStyle(color=ft.Colors.WHITE60, size=16),
                    bgcolor=ft.Colors.TRANSPARENT,
                    border_color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                    focused_border_color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
                    focused_border_width=1.4,
                    content_padding=ft.padding.symmetric(horizontal=10, vertical=15),
                    text_style=ft.TextStyle(size=16),
                ),
                
                ft.Container(height=25),  # Spacing before login button
                
                # Login button
                ft.Container(
                    content=ft.Text(
                        "Log in",
                        color=ft.Colors.WHITE,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor='#0064E0',
                    border_radius=25,
                    height=55,
                    alignment=ft.alignment.center,
                    on_click=lambda _: print('Login button clicked!'),
                ),
                
                ft.Container(height=20),  # Spacing before forgot password
                
                # Forgot password link
                ft.TextButton(
                    "Forgotten password?",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE70,
                        overlay_color=ft.Colors.TRANSPARENT,
                    ),
                    on_click=lambda _: print('Forgot password clicked!'),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        ),
        padding=ft.padding.symmetric(horizontal=5),
    )
    
    # Bottom spacer container
    bottom_spacer = ft.Container(
        content=ft.Text(""),  # Empty content for spacing
        expand=1,
    )
    
    # Create account and Meta section
    bottom_section = ft.Container(
        content=ft.Column(
            [
                ft.Container(height=30),  # Spacing after divider
                
                # Create account button
                ft.Container(
                    content=ft.Text(
                        "Create new account",
                        color="#0064E0",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor=ft.Colors.TRANSPARENT,
                    border=ft.border.all(2, "#0064E0"),
                    border_radius=25,
                    height=55,
                    width=370,
                    alignment=ft.alignment.center,
                    on_click=lambda _: print('Create account clicked!'),
                ),
                
                ft.Container(height=30),  # Spacing before Meta logo
                
                # Meta logo
                ft.Container(
                    content=ft.Image(
                        src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Meta_Platforms_Inc._logo.svg/2560px-Meta_Platforms_Inc._logo.svg.png',
                        height=20,
                        width=60,
                        fit=ft.ImageFit.CONTAIN,
                        color=ft.Colors.WHITE60,
                    ),
                    alignment=ft.alignment.center,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        ),
        padding=ft.padding.symmetric(horizontal=10),
    )
    
    # Language selector for AppBar
    language_selector = ft.Container(
        content=ft.Text("English (UK) ▼", color=ft.Colors.WHITE60, size=14),
        alignment=ft.alignment.center,
    )
    
    # Main layout with SPACE_BETWEEN for perfect responsive design
    main_content = ft.Column(
        [
            top_spacer,           # Top flexible space
            insta_logo_container, # Instagram logo
            middle_spacer,        # Middle flexible space
            login_section,        # Login form section
            bottom_spacer,        # Bottom flexible space
            bottom_section,       # Create account and Meta
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    return ft.View(
        route="/login",
        controls=[main_content],
        appbar=ft.AppBar(
            title=ft.Row([language_selector], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.Colors.TRANSPARENT, 
            elevation_on_scroll=0
        ),
        bgcolor='#152127',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        padding=ft.padding.all(20),
    )