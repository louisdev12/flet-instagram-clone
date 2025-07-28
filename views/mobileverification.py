import flet as ft

def mobileverification_view(page: ft.Page):
    # Create 6 text fields for verification code
    verification_fields = []
    
    def create_verification_field(index):
        field = ft.TextField(
            width=50,
            height=60,
            text_align=ft.TextAlign.CENTER,
            keyboard_type=ft.KeyboardType.NUMBER,
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.WHITE,
            bgcolor=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.WHITE,
            focused_border_width=2,
            border_color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
            border_radius=12,
            text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
            content_padding=ft.padding.all(0),
            max_length=1,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        
        def on_change(e):
            # Auto-focus next field when digit is entered
            if len(e.control.value) == 1 and index < 5:
                verification_fields[index + 1].focus()
            # Auto-focus previous field when backspace is pressed
            elif len(e.control.value) == 0 and index > 0:
                verification_fields[index - 1].focus()
        
        def on_submit(e):
            # Move to next field on enter or auto-submit when all fields are filled
            if index < 5:
                verification_fields[index + 1].focus()
            else:
                # Check if all fields are filled
                code = ''.join([field.value or '' for field in verification_fields])
                if len(code) == 6:
                    verify_code(code)
        
        field.on_change = on_change
        field.on_submit = on_submit
        return field
    
    # Create all 6 verification fields
    for i in range(6):
        verification_fields.append(create_verification_field(i))
    
    def verify_code(code):
        print(f'Verification code entered: {code}')
        # Add your verification logic here
        # For example: page.go('/profile') or make API call
    
    def resend_code():
        # Clear all fields and show resend message
        for field in verification_fields:
            field.value = ''
        page.update()
    
    def open_confirm_number_sheet(e):
        page.open(confirm_number_bs)
    
    def handle_confirm_number(e):
        page.close(confirm_number_bs)
        resend_code()
        # Show success message
        page.open(
            ft.SnackBar(
                content=ft.Text("Verification code sent to +1234567890", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN,
            )
        )
    
    # Top section with title and description
    top_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Enter the confirmation code", 
                    size=24, 
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.LEFT,
                ),
                ft.Container(height=15),
                ft.Text(
                    "To confirm your account, enter the 6 digit code that we sent via WhatsApp to +1234567890",
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
    
    # Verification code input fields
    verification_section = ft.Container(
        content=ft.Row(
            verification_fields,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=10,
        ),
        width=370,
        padding=ft.padding.symmetric(horizontal=5),
    )
    
    # Next button
    def handle_next_click(e):
        code = ''.join([field.value or '' for field in verification_fields])
        if len(code) == 6:
            verify_code(code)
            page.go("/createpassword")
        else:
            # Show error or highlight empty fields
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please enter all 6 digits"),
                    bgcolor=ft.Colors.RED_400,
                )
            )
    
    next_button = ft.Container(
        content=ft.Text(
            "Verify",
            color=ft.Colors.WHITE,
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
        bgcolor='#0064E0',
        border_radius=25,
        height=55,
        width=370,
        alignment=ft.alignment.center,
        on_click=handle_next_click,
    )
    
    # Resend code button
    resend_button = ft.Container(
        content=ft.Text(
            "I didn't receive the code",
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
        on_click=open_confirm_number_sheet,
    )
    
    # Confirm number button for bottom sheet
    confirm_button = ft.ElevatedButton(
        content=ft.Text(
            "Send code to +1234567890",
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
        width=350,
        on_click=handle_confirm_number,
    )
    
    # Bottom sheet for confirming number
    confirm_number_bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Confirm your number", size=22, weight=ft.FontWeight.BOLD),
                    ft.Container(height=15),
                    ft.Text(
                        "We'll send a verification code to confirm this is your phone number. Standard message and data rates may apply.", 
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Text(
                            "+1234567890",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        border_radius=12,
                        padding=ft.padding.symmetric(horizontal=20, vertical=15),
                        width=350,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=30),
                    ft.Column([
                        confirm_button,
                        ft.Container(height=15),
                        ft.TextButton(
                            "Edit number",
                            style=ft.ButtonStyle(
                                overlay_color=ft.Colors.TRANSPARENT,
                            ),
                            on_click=lambda _: (page.close(confirm_number_bs), page.go("/signupphone")),
                        ),
                        ft.Container(height=30),
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            ),
            padding=ft.padding.only(top=20, left=20, right=20, bottom=50),
            expand=True
        ),
        open=False,
        dismissible=True,
        show_drag_handle=True,
        enable_drag=True,
    )
    
    # Timer section for resend countdown (optional)
    timer_section = ft.Container(
        content=ft.Text(
            "Resend code in 60 seconds",
            size=13,
            color=ft.Colors.WHITE60,
            text_align=ft.TextAlign.CENTER,
        ),
        width=370,
        padding=ft.padding.symmetric(horizontal=5),
        alignment=ft.alignment.center,
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
            ft.Container(height=30),  # Extra spacing
            verification_section,   # 6-digit verification fields
            ft.Container(height=20),  # Spacing
            next_button,           # Verify button
            resend_button,         # Resend button
            ft.Container(height=30),
            timer_section,
            middle_spacer,         # Flexible spacer
            bottom_section,        # Already have account link
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    # Auto-focus first field after a short delay
    def auto_focus_first_field():
        import time
        time.sleep(0.1)  # Small delay to ensure view is rendered
        verification_fields[0].focus()
        page.update()
    
    # Start auto-focus in background
    import threading
    threading.Thread(target=auto_focus_first_field, daemon=True).start()
    
    return ft.View(
        route="/mobileverification",
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