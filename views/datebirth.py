import flet as ft
import datetime

def datebirth_view(page: ft.Page):
    # State to hold the selected date
    selected_date = ft.Ref[ft.Text]()
    date_field = ft.Ref[ft.TextField]()
    
    def handle_date_change(e):
        # Update the text field with the selected date
        if e.control.value:
            formatted_date = e.control.value.strftime("%d/%m/%Y")
            date_field.current.value = formatted_date
            page.update()
    
    def handle_date_dismiss(e):
        # Handle when date picker is dismissed
        page.update()
    
    def open_date_picker(e):
        # Open the date picker
        page.open(
            ft.DatePicker(
                first_date=datetime.datetime(1900, 1, 1),
                last_date=datetime.datetime.now(),
                date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR,
                on_change=handle_date_change,
                on_dismiss=handle_date_dismiss,
            )
        )
    
    # Top section with title and description
    top_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "What's your date of birth", 
                    size=24, 
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.LEFT,
                ),
                ft.Container(height=15),
                ft.Column([
                    ft.Text(
                        "Use your own date of birth, even if this account is for a business, a pet or something else. No one will see this unless you choose to share it.", 
                        size=15,
                        color=ft.Colors.WHITE70,
                        text_align=ft.TextAlign.LEFT,
                    ),
                    ft.TextButton("Why do I need to provide my date of birth?",
                        style=ft.ButtonStyle(
                            color="#0064E0",
                            overlay_color=ft.Colors.TRANSPARENT,
                        )
                    )
                ])
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=0,
        ),
        width=370,
        padding=ft.padding.symmetric(horizontal=5),
    )
    
    # Date input field with date picker
    date_input = ft.Container(
        content=ft.TextField(
            ref=date_field,
            hint_text='Date of birth',
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
            read_only=True,  # Make it read-only so users can only select via date picker
            on_click=open_date_picker,  # Open date picker when clicked
            suffix=ft.Icon(
                ft.Icons.CALENDAR_TODAY,
                color=ft.Colors.WHITE70,
                size=20,
            ),
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
        on_click=lambda e: page.go("/username"),
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
            date_input,            # Date input with picker
            next_button,           # Next button
            middle_spacer,         # Flexible spacer
            bottom_section,        # Already have account link
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    return ft.View(
        route="/datebirth",
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