import flet as ft
import asyncio

def splash_view(page: ft.Page):
    # Instagram logo image
    insta_logo = ft.Container(
        content=ft.Image(
            src="https://i.imgur.com/s3WlxzH.png",  # Correct direct image URL
            width=100,
            height=100,
        ),
        alignment=ft.alignment.center,
    )

    # Splash content (spaced layout)
    splash_content = ft.Column(
        [
            ft.Container(),  # Empty container at top
            insta_logo,      # Instagram logo at center
            ft.Container(    # Bottom image with some padding from bottom
                content=ft.Image(
                    src="https://i.imgur.com/Pv5sDen.png",
                    fit=ft.ImageFit.CONTAIN,
                    width=100, 
                    height=100
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=30),  # Add some space from bottom
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    # Auto-navigate to login after 4 seconds
    async def auto_navigate():
        await asyncio.sleep(4)
        page.go("/login")

    page.run_task(auto_navigate)

    return ft.View(
        route="/",
        controls=[
            ft.Container(
                content=splash_content,
                alignment=ft.alignment.center,
                expand=True,
            )
        ],
        bgcolor=ft.Colors.BLACK,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        padding=20,
    )