import flet as ft
from views.splash import splash_view
from views.login import login_view
from views.signupphone import signupphone_view
from views.signupemail import signupemail_view
from views.mobileverification import mobileverification_view
from views.createpassword import createpassword_view
from views.datebirth import datebirth_view

# Entry point for the Flet app
def main(page: ft.Page):
    # Basic window properties
    page.title = "Flet App"
    page.window_width = 400
    page.window_height = 700
    page.padding = 0    
    page.spacing = 0
    page.scroll = ft.ScrollMode.HIDDEN  # Disable scrolling
    page.bgcolor = ft.Colors.TRANSPARENT  # Transparent background (for custom styling)
    page.safe_area = True  # Avoid overlap with system UI (e.g. notches)
    page.window.to_front()  # Bring window to the front
    page.theme_mode = ft.ThemeMode.DARK  # Use dark mode
    page.notch_shape = ft.NotchShape.AUTO  # Auto-detect notch shape

    # ✅ Add custom font
    page.fonts = {
        "Great Vibes": "https://raw.githubusercontent.com/google/fonts/master/ofl/greatvibes/GreatVibes-Regular.ttf"
    }

    # ✅ Apply unified dark theme and page transition animations
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.CUPERTINO,  # Smooth iOS-style transitions
        ),
        scrollbar_theme=ft.ScrollbarTheme(thickness=0.0)  # Hide scrollbars
    )

    # ✅ Define how routes map to views
    def route_change(route):
        page.views.clear()  # Clear current views
        if page.route == "/":
            page.views.append(splash_view(page))  # Show splash screen
        elif page.route == "/login":
            page.views.append(login_view(page))  # Show splash screen
        elif page.route == "/signupphone":
            page.views.append(signupphone_view(page))  # Show splash screen
        elif page.route == "/signupemail":
            page.views.append(signupemail_view(page))  # Show splash screen
        elif page.route == "/mobileverification":
            page.views.append(mobileverification_view(page))  # Show splash screen
        elif page.route == "/createpassword":
            page.views.append(createpassword_view(page))  # Show splash screen
        elif page.route == "/datebirth":
            page.views.append(datebirth_view(page))  # Show splash screen
        page.update()  # Apply changes

    # ✅ Handle view stack popping (e.g. back button)
    def view_pop(view):
        page.views.pop()  # Remove current view
        top_view = page.views[-1]  # Get the previous view
        page.go(top_view.route)  # Navigate back to it

    # Register event handlers
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Navigate to the initial route
    page.go("/")

# Launch the Flet application
ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)