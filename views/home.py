import flet as ft
import random

PRIMARY_COLOR = "#1DA1F2"
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"
DARK_GRAY = "#1C1C1E"

# Global state for liked posts (you might want to use a more sophisticated state management)
liked_posts = set()
current_tab = 0

def instagram_home_view(page: ft.Page):
    """
    Main Instagram home view function that returns a ft.View
    Compatible with your routing system
    """
    
    # Tech accounts data
    tech_accounts = [
        {"name": "github", "username": "github", "verified": True},
        {"name": "stackoverflow", "username": "stackoverflow", "verified": True},
        {"name": "python_dev", "username": "python.dev", "verified": False},
        {"name": "reactjs", "username": "reactjs", "verified": True},
        {"name": "nodejs", "username": "nodejs", "verified": True},
        {"name": "tensorflow", "username": "tensorflow", "verified": True},
        {"name": "docker", "username": "docker", "verified": False},
        {"name": "vscode", "username": "code", "verified": True},
    ]
    
    # Post content data
    post_content = [
        {"type": "code", "content": "# Python Flask App\nfrom flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef hello():\n    return 'Hello World!'"},
        {"type": "design", "content": "🎨 New UI Design System\n✨ Dark Mode\n🚀 Modern Components\n💫 Smooth Animations"},
        {"type": "tech", "content": "🔥 Latest Tech Stack:\n• React 18\n• TypeScript\n• Tailwind CSS\n• Next.js 13"},
        {"type": "tip", "content": "💡 Pro Tip: Use git stash\nto temporarily save changes\nwithout committing"},
        {"type": "code", "content": "// React Hook Example\nimport { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return <button onClick={() => setCount(count + 1)}>\n    Count: {count}\n  </button>;\n}"},
        {"type": "tech", "content": "🚀 DevOps Pipeline:\n• GitHub Actions\n• Docker Containers\n• Kubernetes\n• AWS/Azure Deploy"},
    ]

    def styled_text(text, size=14, color=TEXT_COLOR, weight=None):
        return ft.Text(text, size=size, color=color, weight=weight)

    def toggle_like(post_id):
        global liked_posts
        if post_id in liked_posts:
            liked_posts.remove(post_id)
        else:
            liked_posts.add(post_id)
        page.update()

    def on_tab_change(e):
        global current_tab
        current_tab = e.control.selected_index
        page.update()

    # HOME FEED
    def create_home_feed():
        stories = create_stories()
        
        # Posts
        posts = []
        for i in range(6):
            account = tech_accounts[i % len(tech_accounts)]
            content = post_content[i % len(post_content)]
            posts.append(create_post(account, content, i))

        feed_content = ft.Column([
            stories,
            *posts
        ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)

        return ft.Column([
            ft.Container(content=feed_content, expand=True)
        ], spacing=0, expand=True)

    def create_stories():
        stories = []
        colors = [ft.Colors.PINK_400, ft.Colors.PURPLE_400, ft.Colors.ORANGE_400, ft.Colors.BLUE_400, ft.Colors.GREEN_400]
        
        # Your story
        your_story = ft.Container(
            content=ft.Column([
                ft.Stack([
                    ft.Container(
                        width=60, height=60, border_radius=30,
                        bgcolor=colors[0], alignment=ft.alignment.center,
                        content=ft.Text("Y", size=20, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.ADD, color=PRIMARY_COLOR, size=20),
                        width=20, height=20, bgcolor=BG_COLOR, border_radius=10,
                        border=ft.border.all(2, BG_COLOR),
                        right=0, bottom=0
                    )
                ], width=60, height=60),
                styled_text("Your story", size=12)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            margin=ft.margin.only(right=10)
        )
        stories.append(your_story)
        
        for i, account in enumerate(tech_accounts[:4]):
            story = ft.Container(
                content=ft.Column([
                    ft.Container(
                        width=60, height=60, border_radius=30,
                        bgcolor=colors[(i+1) % len(colors)], alignment=ft.alignment.center,
                        border=ft.border.all(2, ft.Colors.PINK_400),
                        content=ft.Text(account["name"][0].upper(), size=20, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
                    ),
                    styled_text(account["name"], size=12)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                margin=ft.margin.only(right=10)
            )
            stories.append(story)
        
        return ft.Container(
            content=ft.Row(stories, scroll=ft.ScrollMode.HIDDEN),
            padding=ft.padding.symmetric(horizontal=15, vertical=10),
            bgcolor=BG_COLOR
        )

    def create_post(account, content_data, post_id):
        colors = [ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400, ft.Colors.ORANGE_400, ft.Colors.PINK_400]
        avatar_color = colors[hash(account["name"]) % len(colors)]
        
        # Post header
        post_header = ft.Row([
            ft.Container(
                width=35, height=35, border_radius=17.5,
                bgcolor=avatar_color, alignment=ft.alignment.center,
                content=ft.Text(account["name"][0].upper(), size=16, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
            ),
            ft.Container(width=10),
            ft.Column([
                ft.Row([
                    styled_text(account["name"], weight=ft.FontWeight.BOLD),
                    ft.Icon(ft.Icons.VERIFIED, color=PRIMARY_COLOR, size=16) if account["verified"] else ft.Container(),
                ], spacing=5),
                styled_text("Original audio", size=12, color=ft.Colors.WHITE60)
            ], spacing=2),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.Icons.MORE_HORIZ, icon_color=TEXT_COLOR, icon_size=20)
        ], scroll=ft.ScrollMode.HIDDEN)
        
        # Post content
        page_width = page.window.width or 390
        if content_data["type"] == "code":
            post_image = ft.Container(
                content=ft.Container(
                    content=ft.Text(content_data["content"], size=12, color=ft.Colors.GREEN_300, font_family="monospace"),
                    bgcolor="#0D1117", padding=ft.padding.all(15), border_radius=8,
                    width=page_width-40
                ),
                width=page_width-40, height=300, bgcolor=DARK_GRAY,
                alignment=ft.alignment.center, border_radius=8
            )
        else:
            post_image = ft.Container(
                content=ft.Column([
                    ft.Text(content_data["content"], size=16, color=TEXT_COLOR, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    ft.Text("@TECHCOMMUNITY", size=12, color=ft.Colors.WHITE60)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                width=page_width-40, height=300, 
                bgcolor=ft.Colors.with_opacity(0.1, colors[random.randint(0, len(colors)-1)]),
                alignment=ft.alignment.center, border_radius=8
            )
        
        # Like button with state
        is_liked = post_id in liked_posts
        like_button = ft.IconButton(
            icon=ft.Icons.FAVORITE if is_liked else ft.Icons.FAVORITE_BORDER,
            icon_color=ft.Colors.RED if is_liked else TEXT_COLOR,
            icon_size=28,
            on_click=lambda _: toggle_like(post_id)
        )
        
        # Post actions
        post_actions = ft.Row([
            ft.Row([
                like_button,
                ft.IconButton(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, icon_color=TEXT_COLOR, icon_size=28),
                ft.IconButton(icon=ft.Icons.SEND, icon_color=TEXT_COLOR, icon_size=28),
            ], spacing=0),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.Icons.BOOKMARK_BORDER, icon_color=TEXT_COLOR, icon_size=28)
        ],scroll=ft.ScrollMode.HIDDEN)
        
        # Likes and caption
        likes_count = random.randint(1, 50) + (1 if is_liked else 0)
        post_info = ft.Column([
            styled_text(f"{likes_count} likes", weight=ft.FontWeight.BOLD),
            ft.Container(height=5),
            ft.Row([
                styled_text(account["name"], weight=ft.FontWeight.BOLD),
                styled_text("🚀 Check out our latest updates!", color=ft.Colors.WHITE70)
            ], spacing=5),
            ft.Container(height=5),
            styled_text("View all comments", color=ft.Colors.WHITE60, size=12)
        ], spacing=0,scroll=ft.ScrollMode.HIDDEN)
        
        return ft.Container(
            content=ft.Column([
                post_header,
                ft.Container(height=10),
                post_image,
                ft.Container(height=10),
                post_actions,
                post_info,
                ft.Container(height=20)
            ]),
            padding=ft.padding.symmetric(horizontal=15),
            bgcolor=BG_COLOR
        )

    # SEARCH PAGE
    def create_search_page():
        search_bar = ft.Container(
            content=ft.TextField(
                hint_text="Search",
                hint_style=ft.TextStyle(color=ft.Colors.WHITE60),
                text_style=ft.TextStyle(color=TEXT_COLOR),
                bgcolor=DARK_GRAY,
                border_color=ft.Colors.TRANSPARENT,
                focused_border_color=ft.Colors.TRANSPARENT,
                prefix_icon=ft.Icons.SEARCH,
                border_radius=10,
                content_padding=ft.padding.symmetric(horizontal=15, vertical=12)
            ),
            padding=ft.padding.all(15)
        )

        # Create grid of posts
        grid_items = []
        colors = [ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400, ft.Colors.ORANGE_400, ft.Colors.PINK_400, ft.Colors.CYAN_400]
        
        for i in range(12):
            account = tech_accounts[i % len(tech_accounts)]
            grid_items.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"#{account['name']}", size=14, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                        ft.Container(height=5),
                        ft.Text("🔥", size=30)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    width=120, height=120,
                    bgcolor=colors[i % len(colors)],
                    border_radius=8,
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(2)
                )
            )

        grid = ft.GridView(
            grid_items,
            runs_count=3,
            max_extent=120,
            child_aspect_ratio=1,
            spacing=4,
            run_spacing=4,
            expand=True
        )

        return ft.Column([
            search_bar,
            ft.Container(content=grid, expand=True, padding=ft.padding.symmetric(horizontal=15))
        ], expand=True)

    # REELS PAGE
    def create_reels_page():
        reels = []
        for i in range(5):
            account = tech_accounts[i % len(tech_accounts)]
            reel = ft.Container(
                content=ft.Stack([
                    ft.Container(
                        width=page.window.width or 390,
                        height=600,
                        bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_400),
                        content=ft.Column([
                            ft.Text("🎬", size=60),
                            ft.Text(f"{account['name']} Reel", size=20, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                            ft.Text("Coding Tutorial", size=16, color=ft.Colors.WHITE70)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_color=TEXT_COLOR, icon_size=35),
                            ft.Text("1.2K", color=TEXT_COLOR, size=12),
                            ft.IconButton(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, icon_color=TEXT_COLOR, icon_size=35),
                            ft.Text("89", color=TEXT_COLOR, size=12),
                            ft.IconButton(icon=ft.Icons.SEND, icon_color=TEXT_COLOR, icon_size=35),
                            ft.IconButton(icon=ft.Icons.MORE_VERT, icon_color=TEXT_COLOR, icon_size=35),
                        ]),
                        right=10,
                        bottom=100,
                        alignment=ft.alignment.center
                    )
                ]),
                margin=ft.margin.only(bottom=10)
            )
            reels.append(reel)

        return ft.Column(reels, scroll=ft.ScrollMode.AUTO, expand=True)

    # SHOP PAGE
    def create_shop_page():
        shop_items = []
        products = ["GitHub T-Shirt", "VS Code Mug", "Python Stickers", "React Hoodie", "Node.js Cap", "Docker Bottle"]
        
        for i, product in enumerate(products):
            shop_items.append(
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            width=150, height=150,
                            bgcolor=ft.Colors.GREY_800,
                            border_radius=8,
                            content=ft.Column([
                                ft.Text("🛍️", size=40),
                                ft.Text(product, size=12, color=TEXT_COLOR, text_align=ft.TextAlign.CENTER)
                            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                        ),
                        ft.Text(f"${random.randint(10, 50)}", size=16, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
                    ]),
                    margin=ft.margin.all(5)
                )
            )

        grid = ft.GridView(
            shop_items,
            runs_count=2,
            max_extent=160,
            child_aspect_ratio=0.8,
            spacing=10,
            run_spacing=10,
            expand=True
        )

        return ft.Column([
            ft.Container(
                content=ft.Text("Shop", size=24, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                padding=ft.padding.all(15)
            ),
            ft.Container(content=grid, expand=True, padding=ft.padding.symmetric(horizontal=15))
        ], expand=True)

    # PROFILE PAGE
    def create_profile_page():
        return ft.Column([
            # Profile Header
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            width=80, height=80, border_radius=40,
                            bgcolor=ft.Colors.ORANGE_400, alignment=ft.alignment.center,
                            content=ft.Text("P", size=32, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
                        ),
                        ft.Container(width=20),
                        ft.Column([
                            ft.Row([
                                ft.Column([ft.Text("150", size=18, weight=ft.FontWeight.BOLD, color=TEXT_COLOR), ft.Text("posts", size=14, color=ft.Colors.WHITE70)]),
                                ft.Container(width=20),
                                ft.Column([ft.Text("1.2K", size=18, weight=ft.FontWeight.BOLD, color=TEXT_COLOR), ft.Text("followers", size=14, color=ft.Colors.WHITE70)]),
                                ft.Container(width=20),
                                ft.Column([ft.Text("500", size=18, weight=ft.FontWeight.BOLD, color=TEXT_COLOR), ft.Text("following", size=14, color=ft.Colors.WHITE70)])
                            ])
                        ])
                    ],scroll=ft.ScrollMode.HIDDEN),
                    ft.Container(height=15),
                    ft.Column([
                        ft.Text("Python Developer", size=16, weight=ft.FontWeight.BOLD, color=TEXT_COLOR),
                        ft.Text("🐍 Python | 🚀 Flask | ⚛️ React", size=14, color=ft.Colors.WHITE70),
                        ft.Text("Building awesome apps with Flet!", size=14, color=ft.Colors.WHITE70)
                    ], alignment=ft.MainAxisAlignment.START),
                    ft.Container(height=15),
                    ft.ElevatedButton("Edit Profile", bgcolor=DARK_GRAY, color=TEXT_COLOR, width=200)
                ]),
                padding=ft.padding.all(15)
            ),
            
            # Posts Grid
            ft.Container(
                content=ft.GridView([
                    ft.Container(width=120, height=120, bgcolor=ft.Colors.BLUE_400, border_radius=4, 
                               content=ft.Text("📱", size=30), alignment=ft.alignment.center),
                    ft.Container(width=120, height=120, bgcolor=ft.Colors.GREEN_400, border_radius=4,
                               content=ft.Text("💻", size=30), alignment=ft.alignment.center),
                    ft.Container(width=120, height=120, bgcolor=ft.Colors.PURPLE_400, border_radius=4,
                               content=ft.Text("🔥", size=30), alignment=ft.alignment.center),
                    ft.Container(width=120, height=120, bgcolor=ft.Colors.ORANGE_400, border_radius=4,
                               content=ft.Text("⚡", size=30), alignment=ft.alignment.center),
                    ft.Container(width=120, height=120, bgcolor=ft.Colors.PINK_400, border_radius=4,
                               content=ft.Text("🚀", size=30), alignment=ft.alignment.center),
                    ft.Container(width=120, height=120, bgcolor=ft.Colors.CYAN_400, border_radius=4,
                               content=ft.Text("🎨", size=30), alignment=ft.alignment.center)
                ], runs_count=3, max_extent=120, child_aspect_ratio=1, spacing=2, run_spacing=2),
                expand=True,
                padding=ft.padding.symmetric(horizontal=5)
            )
        ], expand=True)

    # Create content based on current tab
    if current_tab == 0:
        content = create_home_feed()
    elif current_tab == 1:
        content = create_search_page()
    elif current_tab == 2:
        content = create_reels_page()
    elif current_tab == 3:
        content = create_shop_page()
    else:
        content = create_profile_page()

    # Cupertino Bottom Navigation
    bottom_nav = ft.CupertinoNavigationBar(
        bgcolor=BG_COLOR,
        inactive_color=ft.Colors.WHITE60,
        active_color=TEXT_COLOR,
        selected_index=current_tab,
        on_change=on_tab_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.PLAY_CIRCLE_OUTLINE, label="Reels"),
            ft.NavigationBarDestination(icon=ft.Icons.CHAT_BUBBLE, label="Messages"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile")
        ]
    )

    # Return the main view
    return ft.View(
        route="/instagram_home",
        controls=[
            ft.Column([
                ft.Container(content=content, expand=True),
                bottom_nav
            ], spacing=0, expand=True)
        ],
        scroll=ft.ScrollMode.HIDDEN,
        appbar = ft.AppBar(
            toolbar_height=56,
            bgcolor=ft.Colors.TRANSPARENT,
            elevation_on_scroll=0,
            title=ft.Text(
                "Instagram",
                size=28,
                color=TEXT_COLOR,
                weight=ft.FontWeight.BOLD,
                font_family="Great Vibes",
            ),
            actions=[
                ft.IconButton(icon=ft.Icons.ADD_BOX_OUTLINED, icon_color=TEXT_COLOR, icon_size=28),
                ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_color=TEXT_COLOR, icon_size=28, badge=ft.Badge(bgcolor=ft.Colors.RED, small_size=10,alignment=ft.alignment.top_right, padding=5)),
            ]
        ),
        bgcolor=BG_COLOR,
        padding=ft.padding.all(0)
    )