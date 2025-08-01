import flet as ft
import random
import datetime

# Enhanced color scheme and constants
PRIMARY_COLOR = "#1DA1F2"
TEXT_COLOR = ft.Colors.WHITE
BG_COLOR = "#000000"
DARK_GRAY = "#1C1C1E"
CARD_BG = "#0A0A0A"
ACCENT_COLOR = "#FF3040"
VERIFIED_COLOR = "#1D9BF0"

# Global state management
class AppState:
    def __init__(self):
        self.liked_posts = set()
        self.bookmarked_posts = set()
        self.following_accounts = set()
        self.current_tab = 0
        self.story_viewed = set()

app_state = AppState()

def styled_text(text, size=14, color=TEXT_COLOR, weight=None):
    return ft.Text(
        text,
        size=size,
        color=color,
        weight=weight,
        overflow=ft.TextOverflow.ELLIPSIS
    )

def toggle_like(post_id):
    if post_id in app_state.liked_posts:
        app_state.liked_posts.remove(post_id)
    else:
        app_state.liked_posts.add(post_id)

def toggle_bookmark(post_id):
    if post_id in app_state.bookmarked_posts:
        app_state.bookmarked_posts.remove(post_id)
    else:
        app_state.bookmarked_posts.add(post_id)

def toggle_follow(account_name):
    if account_name in app_state.following_accounts:
        app_state.following_accounts.remove(account_name)
    else:
        app_state.following_accounts.add(account_name)

def on_tab_change(e, page):
    app_state.current_tab = e.control.selected_index
    page.update()

def show_comments_sheet(post_id, account_name, page):
    """Show comments bottom sheet"""
    comments = [
        {"user": "john_doe", "text": "Great post! 🔥", "time": "2h"},
        {"user": "jane_dev", "text": "Thanks for sharing this!", "time": "1h"},
        {"user": "code_master", "text": "Very helpful tutorial 👍", "time": "45m"},
    ]

    comment_items = []
    for comment in comments:
        comment_items.append(
            ft.ListTile(
                leading=ft.Container(
                    width=32, height=32, border_radius=16,
                    bgcolor=ft.Colors.BLUE_400,
                    content=ft.Text(comment["user"][0].upper(), size=14, color=TEXT_COLOR),
                    alignment=ft.alignment.center
                ),
                title=ft.Row([
                    styled_text(comment["user"], weight=ft.FontWeight.BOLD),
                    styled_text(comment["time"], size=12, color=ft.Colors.WHITE60)
                ]),
                subtitle=styled_text(comment["text"], size=14),
            )
        )

    page.open(
        ft.BottomSheet(
            content=ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=styled_text("Comments", size=18, weight=ft.FontWeight.BOLD),
                        padding=ft.padding.all(15),
                        alignment=ft.alignment.center
                    ),
                    ft.Divider(color=DARK_GRAY, height=1),
                    ft.Column(comment_items, scroll=ft.ScrollMode.AUTO, height=300),
                    ft.Container(
                        content=ft.Row([
                            ft.TextField(
                                hint_text="Add a comment...",
                                hint_style=ft.TextStyle(color=ft.Colors.WHITE60),
                                text_style=ft.TextStyle(color=TEXT_COLOR),
                                bgcolor=DARK_GRAY,
                                border_color=ft.Colors.TRANSPARENT,
                                expand=True
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SEND,
                                icon_color=PRIMARY_COLOR,
                                icon_size=24
                            )
                        ]),
                        padding=ft.padding.all(15)
                    )
                ]),
                bgcolor=BG_COLOR,
                padding=ft.padding.all(0)
            ),
            open=True
        )
    )

def create_post(account, content_data, post_id, page):
    colors = [
        ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400,
        ft.Colors.ORANGE_400, ft.Colors.PINK_400, ft.Colors.CYAN_400,
        ft.Colors.INDIGO_400, ft.Colors.TEAL_400
    ]
    avatar_color = colors[hash(account["name"]) % len(colors)]

    # Enhanced post header with follow button
    is_following = account["name"] in app_state.following_accounts
    follow_button = ft.TextButton(
        text="Following" if is_following else "Follow",
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE60 if is_following else PRIMARY_COLOR,
            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD)
        ),
        on_click=lambda _: toggle_follow(account["name"])
    ) if account["name"] != "your_account" else ft.Container()

    post_header = ft.Container(
        content=ft.Row([
            ft.Container(
                width=40, height=40, border_radius=20,
                bgcolor=avatar_color, alignment=ft.alignment.center,
                content=ft.Text(
                    account["name"][0].upper(),
                    size=18,
                    color=TEXT_COLOR,
                    weight=ft.FontWeight.BOLD
                ),
                border=ft.border.all(2, colors[hash(account["name"]) % len(colors)])
            ),
            ft.Container(width=12),
            ft.Column([
                ft.Row([
                    styled_text(account["name"], weight=ft.FontWeight.BOLD, size=15),
                    ft.Icon(
                        ft.Icons.VERIFIED,
                        color=VERIFIED_COLOR,
                        size=16
                    ) if account["verified"] else ft.Container(),
                ], spacing=5),
                styled_text(
                    f"{account.get('followers', '0')} followers",
                    size=12,
                    color=ft.Colors.WHITE60
                )
            ], spacing=2),
            ft.Container(expand=True),
            follow_button,
            ft.IconButton(
                icon=ft.Icons.MORE_VERT,
                icon_color=TEXT_COLOR,
                icon_size=20
            )
        ], scroll=ft.ScrollMode.HIDDEN),
        padding=ft.padding.symmetric(horizontal=15, vertical=12)
    )

    # Enhanced post content with better styling
    page_width = page.window.width or 390

    if content_data["type"] == "code":
        post_image = ft.Container(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            width=12, height=12, border_radius=6,
                            bgcolor=ft.Colors.RED_400
                        ),
                        ft.Container(
                            width=12, height=12, border_radius=6,
                            bgcolor=ft.Colors.YELLOW_400
                        ),
                        ft.Container(
                            width=12, height=12, border_radius=6,
                            bgcolor=ft.Colors.GREEN_400
                        ),
                    ], spacing=8),
                    ft.Container(height=10),
                    ft.Text(
                        content_data["content"],
                        size=11,
                        color=ft.Colors.GREEN_300,
                        font_family="Courier",
                        selectable=True
                    )
                ]),
                bgcolor="#0D1117",
                padding=ft.padding.all(15),
                border_radius=12,
                width=page_width-30,
                border=ft.border.all(1, "#30363D")
            ),
            width=page_width-30,
            height=320,
            bgcolor=CARD_BG,
            alignment=ft.alignment.top_center,
            border_radius=12,
            padding=ft.padding.all(15)
        )
    else:
        post_image = ft.Container(
            content=ft.Column([
                ft.Text(
                    content_data["content"],
                    size=16,
                    color=TEXT_COLOR,
                    text_align=ft.TextAlign.LEFT,
                    weight=ft.FontWeight.W_400
                ),
                ft.Container(height=20),
                ft.Container(
                    content=styled_text(
                        f"@{account['username']}",
                        size=12,
                        color=ft.Colors.WHITE60
                    ),
                    alignment=ft.alignment.bottom_right
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            width=page_width-30,
            height=280,
            bgcolor=ft.Colors.with_opacity(0.05, colors[random.randint(0, len(colors)-1)]),
            alignment=ft.alignment.center,
            border_radius=12,
            padding=ft.padding.all(20),
            border=ft.border.all(1, ft.Colors.with_opacity(0.1, TEXT_COLOR))
        )

    # Enhanced post actions with animations
    is_liked = post_id in app_state.liked_posts
    is_bookmarked = post_id in app_state.bookmarked_posts

    like_button = ft.IconButton(
        icon=ft.Icons.FAVORITE if is_liked else ft.Icons.FAVORITE_BORDER,
        icon_color=ACCENT_COLOR if is_liked else TEXT_COLOR,
        icon_size=28,
        on_click=lambda _: toggle_like(post_id),
        tooltip="Like"
    )

    comment_button = ft.IconButton(
        icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
        icon_color=TEXT_COLOR,
        icon_size=28,
        on_click=lambda _: show_comments_sheet(post_id, account["name"], page),
        tooltip="Comment"
    )

    share_button = ft.IconButton(
        icon=ft.Icons.SEND,
        icon_color=TEXT_COLOR,
        icon_size=28,
        tooltip="Share"
    )

    bookmark_button = ft.IconButton(
        icon=ft.Icons.BOOKMARK if is_bookmarked else ft.Icons.BOOKMARK_BORDER,
        icon_color=TEXT_COLOR,
        icon_size=28,
        on_click=lambda _: toggle_bookmark(post_id),
        tooltip="Save"
    )

    post_actions = ft.Container(
        content=ft.Row([
            ft.Row([
                like_button,
                comment_button,
                share_button,
            ], spacing=5),
            ft.Container(expand=True),
            bookmark_button
        ]),
        padding=ft.padding.symmetric(horizontal=15, vertical=8)
    )

    # Enhanced likes and caption section
    likes_count = random.randint(50, 2500) + (1 if is_liked else 0)
    comments_count = random.randint(5, 150)
    time_ago = random.choice(["2m", "15m", "1h", "3h", "1d", "2d"])

    post_info = ft.Container(
        content=ft.Column([
            styled_text(
                f"{likes_count:,} likes",
                weight=ft.FontWeight.BOLD,
                size=14
            ),
            ft.Container(height=8),
            ft.Row([
                styled_text(account["name"], weight=ft.FontWeight.BOLD, size=14),
                ft.Container(
                    content=styled_text(
                        content_data["caption"],
                        color=ft.Colors.WHITE10,
                        size=14
                    ),
                    expand=True
                )
            ], spacing=8),
            ft.Container(height=5),
            styled_text(
                content_data["hashtags"],
                color=PRIMARY_COLOR,
                size=13
            ),
            ft.Container(height=8),
            styled_text(
                f"View all {comments_count} comments",
                color=ft.Colors.WHITE60,
                size=13
            ),
            ft.Container(height=5),
            styled_text(
                time_ago,
                color=ft.Colors.WHITE38,
                size=12
            )
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=15, vertical=5)
    )

    return ft.Container(
        content=ft.Column([
            post_header,
            post_image,
            post_actions,
            post_info,
            ft.Container(height=15),
            ft.Divider(color=DARK_GRAY, height=1)
        ], spacing=0),
        bgcolor=BG_COLOR,
        margin=ft.margin.only(bottom=5)
    )

def create_stories(page):
    stories = []
    colors = [
        ft.Colors.PINK_400, ft.Colors.PURPLE_400, ft.Colors.ORANGE_400,
        ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.CYAN_400,
        ft.Colors.INDIGO_400, ft.Colors.TEAL_400
    ]

    # Your story with gradient ring
    your_story = ft.Container(
        content=ft.Column([
            ft.Stack([
                ft.Container(
                    width=66, height=66, border_radius=33,
                    bgcolor=colors[0], alignment=ft.alignment.center,
                    border=ft.border.all(3, ft.Colors.PINK_400),
                    content=ft.Text("You", size=12, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.ADD_CIRCLE, color=PRIMARY_COLOR, size=22),
                    width=22, height=22,
                    right=-2, bottom=-2
                )
            ], width=66, height=66),
            styled_text("Your story", size=12)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
        margin=ft.margin.only(right=15)
    )
    stories.append(your_story)

    # Mock tech accounts data for stories
    tech_accounts = [
        {"name": "github", "username": "github", "verified": True, "followers": "2.1M"},
        {"name": "stackoverflow", "username": "stackoverflow", "verified": True, "followers": "1.8M"},
        {"name": "python_dev", "username": "python.dev", "verified": False, "followers": "890K"},
        {"name": "reactjs", "username": "reactjs", "verified": True, "followers": "1.2M"},
        {"name": "nodejs", "username": "nodejs", "verified": True, "followers": "950K"},
        {"name": "tensorflow", "username": "tensorflow", "verified": True, "followers": "780K"},
        {"name": "docker", "username": "docker", "verified": False, "followers": "650K"},
    ]

    # Other stories
    for i, account in enumerate(tech_accounts[:7]):
        is_viewed = account["name"] in app_state.story_viewed
        border_color = DARK_GRAY if is_viewed else colors[(i+1) % len(colors)]

        story = ft.Container(
            content=ft.Column([
                ft.Container(
                    width=66, height=66, border_radius=33,
                    bgcolor=colors[(i+1) % len(colors)],
                    alignment=ft.alignment.center,
                    border=ft.border.all(3, border_color),
                    content=ft.Text(
                        account["name"][:3].upper(),
                        size=12,
                        color=TEXT_COLOR,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                styled_text(
                    account["name"][:8] + ("..." if len(account["name"]) > 8 else ""),
                    size=12
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
            margin=ft.margin.only(right=15),
            on_click=lambda e, name=account["name"]: app_state.story_viewed.add(name) or page.update()
        )
        stories.append(story)

    return ft.Container(
        content=ft.Row(stories, scroll=ft.ScrollMode.HIDDEN),
        padding=ft.padding.symmetric(horizontal=15, vertical=15),
        bgcolor=BG_COLOR
    )

def create_home_feed(page):
    stories = create_stories(page)

    # Mock tech accounts data (should ideally come from a database or API)
    tech_accounts = [
        {"name": "github", "username": "github", "verified": True, "followers": "2.1M", "bio": "Where the world builds software"},
        {"name": "stackoverflow", "username": "stackoverflow", "verified": True, "followers": "1.8M", "bio": "Helping developers learn & share"},
        {"name": "python_dev", "username": "python.dev", "verified": False, "followers": "890K", "bio": "🐍 Python Community Hub"},
        {"name": "reactjs", "username": "reactjs", "verified": True, "followers": "1.2M", "bio": "A JavaScript library for building UIs"},
        {"name": "nodejs", "username": "nodejs", "verified": True, "followers": "950K", "bio": "Node.js JavaScript runtime"},
        {"name": "tensorflow", "username": "tensorflow", "verified": True, "followers": "780K", "bio": "An end-to-end ML platform"},
        {"name": "docker", "username": "docker", "verified": False, "followers": "650K", "bio": "🐳 Containerize everything"},
        {"name": "vscode", "username": "code", "verified": True, "followers": "1.5M", "bio": "Code editor redefined"},
        {"name": "kubernetes", "username": "kubernetesio", "verified": True, "followers": "420K", "bio": "Production-Grade Container Orchestration"},
        {"name": "aws", "username": "awscloud", "verified": True, "followers": "3.2M", "bio": "Amazon Web Services"},
    ]

    # Mock post content
    post_content = [
        {
            "type": "code",
            "content": "# Python Flask REST API\nfrom flask import Flask, jsonify\nfrom flask_restful import Api, Resource\n\napp = Flask(__name__)\napi = Api(app)\n\nclass HelloWorld(Resource):\n    def get(self):\n        return {'message': 'Hello, World!'}\n\napi.add_resource(HelloWorld, '/')\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            "caption": "Building a simple REST API with Flask! 🚀",
            "hashtags": "#Python #Flask #API #WebDev"
        },
        {
            "type": "design",
            "content": "🎨 New Design System 2024\n\n✨ Dark Mode First\n🚀 Micro-interactions\n💫 Glassmorphism UI\n🎯 Accessibility Focus\n📱 Mobile-First Design",
            "caption": "Excited to share our new design system!",
            "hashtags": "#DesignSystem #UI #UX #Design"
        },
        {
            "type": "tech",
            "content": "🔥 Modern Full-Stack:\n\n Frontend:\n• React 18 + TypeScript\n• Next.js 14 (App Router)\n• Tailwind CSS + Headless UI\n\n Backend:\n• Node.js + Express\n• PostgreSQL + Prisma\n• Redis for caching\n\n DevOps:\n• Docker + Kubernetes\n• GitHub Actions\n• AWS/Vercel Deploy",
            "caption": "Our production stack is finally complete! What's your go-to stack?",
            "hashtags": "#FullStack #React #NodeJS #DevOps"
        },
        {
            "type": "tip",
            "content": "💡 Git Pro Tips:\n\n1. Use git stash push -m \"message\"\n   to add descriptive messages\n\n2. git log --oneline --graph\n   for beautiful commit history\n\n3. git bisect for finding bugs\n   in commit history\n\n4. git worktree for multiple\n   working directories",
            "caption": "These Git commands changed my workflow forever!",
            "hashtags": "#Git #ProductivityTips #DevTools"
        },
        {
            "type": "code",
            "content": "// React Custom Hook Example\nimport { useState, useEffect } from 'react';\n\nfunction useLocalStorage(key, initialValue) {\n  const [storedValue, setStoredValue] = useState(() => {\n    try {\n      const item = window.localStorage.getItem(key);\n      return item ? JSON.parse(item) : initialValue;\n    } catch (error) {\n      return initialValue;\n    }\n  });\n\n  const setValue = (value) => {\n    try {\n      setStoredValue(value);\n      window.localStorage.setItem(key, JSON.stringify(value));\n    } catch (error) {\n      console.error(error);\n    }\n  };\n\n  return [storedValue, setValue];\n}",
            "caption": "Custom React hook for localStorage! Super useful for persisting state 💾",
            "hashtags": "#React #Hooks #JavaScript #WebDev"
        },
        {
            "type": "tech",
            "content": "🚀 DevOps Pipeline Evolution:\n\n Stage 1: Manual deploys 😰\n Stage 2: Basic CI/CD 😊\n Stage 3: Infrastructure as Code 🎯\n Stage 4: GitOps + Monitoring 🚀\n Stage 5: AI-Powered DevOps 🤖\n\n Where are you in your journey?",
            "caption": "The DevOps journey is never-ending, but so rewarding!",
            "hashtags": "#DevOps #CI #CD #Infrastructure #Automation"
        },
    ]

    # Posts
    posts = []
    for i in range(8):
        account = tech_accounts[i % len(tech_accounts)]
        content = post_content[i % len(post_content)]
        posts.append(create_post(account, content, i, page))

    feed_content = ft.Column([
        stories,
        *posts
    ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)
    return ft.Container(content=feed_content, expand=True)

def create_search_page(page):
    search_bar = ft.Container(
        content=ft.TextField(
            hint_text="Search accounts, hashtags, and more...",
            hint_style=ft.TextStyle(color=ft.Colors.WHITE60),
            text_style=ft.TextStyle(color=TEXT_COLOR),
            bgcolor=DARK_GRAY,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=PRIMARY_COLOR,
            prefix_icon=ft.Icons.SEARCH,
            border_radius=12,
            content_padding=ft.padding.symmetric(horizontal=15, vertical=15)
        ),
        padding=ft.padding.all(15)
    )

    # Trending hashtags
    trending_tags = ft.Container(
        content=ft.Column([
            styled_text("Trending", size=16, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            ft.Wrap([
                ft.Container(
                    content=styled_text(f"#{tag}", size=14, color=PRIMARY_COLOR),
                    bgcolor=DARK_GRAY,
                    padding=ft.padding.symmetric(horizontal=12, vertical=8),
                    border_radius=20,
                    margin=ft.margin.only(right=8, bottom=8)
                ) for tag in ["Python", "WebDev", "AI", "React", "DevOps", "Design", "JavaScript", "Flutter"]
            ])
        ]),
        padding=ft.padding.symmetric(horizontal=15, vertical=10)
    )

    # Enhanced grid of posts
    grid_items = []
    colors = [
        ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400,
        ft.Colors.ORANGE_400, ft.Colors.PINK_400, ft.Colors.CYAN_400,
        ft.Colors.INDIGO_400, ft.Colors.TEAL_400, ft.Colors.LIME_400,
        ft.Colors.AMBER_400, ft.Colors.DEEP_ORANGE_400, ft.Colors.DEEP_PURPLE_400
    ]

    tech_accounts = [
        {"name": "github", "username": "github"},
        {"name": "stackoverflow", "username": "stackoverflow"},
        {"name": "python_dev", "username": "python.dev"},
        {"name": "reactjs", "username": "reactjs"},
        {"name": "nodejs", "username": "nodejs"},
        {"name": "tensorflow", "username": "tensorflow"},
        {"name": "docker", "username": "docker"},
        {"name": "vscode", "username": "code"},
        {"name": "kubernetes", "username": "kubernetesio"},
        {"name": "aws", "username": "awscloud"},
    ]

    for i in range(15):
        account = tech_accounts[i % len(tech_accounts)]
        grid_items.append(
            ft.Container(
                content=ft.Stack([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("💻", size=20),
                            ft.Container(height=5),
                            ft.Text(f"#{account['name']}", size=11, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                            ft.Text(f"{random.randint(10, 999)}K", size=10, color=ft.Colors.WHITE70)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        width=120, height=120,
                        bgcolor=colors[i % len(colors)],
                        border_radius=12,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, color=TEXT_COLOR, size=20),
                        right=5, top=5
                    ) if i % 3 == 0 else ft.Container()
                ]),
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
        trending_tags,
        ft.Container(content=grid, expand=True, padding=ft.padding.symmetric(horizontal=15))
    ], expand=True)

def create_reels_page(page):
    colors = [
        ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400,
        ft.Colors.ORANGE_400, ft.Colors.PINK_400, ft.Colors.CYAN_400,
        ft.Colors.INDIGO_400, ft.Colors.TEAL_400
    ]

    tech_accounts = [
        {"name": "github", "username": "github"},
        {"name": "stackoverflow", "username": "stackoverflow"},
        {"name": "python_dev", "username": "python.dev"},
        {"name": "reactjs", "username": "reactjs"},
        {"name": "nodejs", "username": "nodejs"},
        {"name": "tensorflow", "username": "tensorflow"},
        {"name": "docker", "username": "docker"},
        {"name": "vscode", "username": "code"},
        {"name": "kubernetes", "username": "kubernetesio"},
        {"name": "aws", "username": "awscloud"},
    ]

    reels = []
    for i in range(6):
        account = tech_accounts[i % len(tech_accounts)]
        view_count = f"{random.randint(10, 999)}K"
        like_count = f"{random.randint(5, 200)}K"

        reel = ft.Container(
            content=ft.Stack([
                ft.Container(
                    width=page.window.width or 390,
                    height=600,
                    bgcolor=ft.Colors.with_opacity(0.3, colors[i % len(colors)]),
                    content=ft.Column([
                        ft.Text("🎬", size=60),
                        ft.Container(height=20),
                        ft.Text(f"{account['name']} Tutorial", size=20, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                        ft.Text("Learn to code in 60 seconds", size=16, color=ft.Colors.WHITE70),
                        ft.Container(height=10),
                        ft.Text(f"👀 {view_count} views", size=14, color=ft.Colors.WHITE60)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
                ),
                # Right side actions
                ft.Container(
                    content=ft.Column([
                        ft.Column([
                            ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_color=TEXT_COLOR, icon_size=35),
                            ft.Text(like_count, color=TEXT_COLOR, size=12, text_align=ft.TextAlign.CENTER),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Container(height=15),
                        ft.Column([
                            ft.IconButton(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, icon_color=TEXT_COLOR, icon_size=35),
                            ft.Text(f"{random.randint(10, 500)}", color=TEXT_COLOR, size=12, text_align=ft.TextAlign.CENTER),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Container(height=15),
                        ft.IconButton(icon=ft.Icons.SEND, icon_color=TEXT_COLOR, icon_size=35),
                        ft.Container(height=15),
                        ft.IconButton(icon=ft.Icons.BOOKMARK_BORDER, icon_color=TEXT_COLOR, icon_size=35),
                        ft.Container(height=15),
                        ft.IconButton(icon=ft.Icons.MORE_VERT, icon_color=TEXT_COLOR, icon_size=35),
                    ]),
                    right=10,
                    bottom=100,
                    alignment=ft.alignment.center
                ),
                # Bottom user info
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            width=35, height=35, border_radius=17.5,
                            bgcolor=colors[hash(account["name"]) % len(colors)],
                            content=ft.Text(account["name"][0].upper(), size=16, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(width=10),
                        ft.Column([
                            styled_text(account["name"], weight=ft.FontWeight.BOLD, size=15),
                            styled_text("💻 Coding Tutorial", size=13, color=ft.Colors.WHITE70)
                        ], spacing=2)
                    ]),
                    left=15,
                    bottom=30,
                    alignment=ft.alignment.center_left
                )
            ]),
            margin=ft.margin.only(bottom=10)
        )
        reels.append(reel)

    return ft.Column(reels, scroll=ft.ScrollMode.AUTO, expand=True)

def create_messages_page(page):
    colors = [
        ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400,
        ft.Colors.ORANGE_400, ft.Colors.PINK_400, ft.Colors.CYAN_400,
        ft.Colors.INDIGO_400, ft.Colors.TEAL_400
    ]

    # Recent conversations
    conversations = [
        {"name": "github", "message": "Thanks for the collaboration!", "time": "2m", "unread": 2},
        {"name": "reactjs", "message": "New React 18 features are amazing", "time": "1h", "unread": 0},
        {"name": "python_dev", "message": "Check out this Python tip!", "time": "3h", "unread": 1},
        {"name": "nodejs", "message": "Server-side rendering is the future", "time": "1d", "unread": 0},
        {"name": "tensorflow", "message": "AI/ML workshop next week!", "time": "2d", "unread": 0},
    ]

    # Search bar
    search_bar = ft.Container(
        content=ft.TextField(
            hint_text="Search messages...",
            hint_style=ft.TextStyle(color=ft.Colors.WHITE60),
            text_style=ft.TextStyle(color=TEXT_COLOR),
            bgcolor=DARK_GRAY,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=PRIMARY_COLOR,
            prefix_icon=ft.Icons.SEARCH,
            border_radius=12,
            content_padding=ft.padding.symmetric(horizontal=15, vertical=12)
        ),
        padding=ft.padding.all(15)
    )

    # Conversation list
    conversation_items = []
    for conv in conversations:
        conversation_items.append(
            ft.Container(
                content=ft.Row([
                    ft.Stack([
                        ft.Container(
                            width=50, height=50, border_radius=25,
                            bgcolor=colors[hash(conv["name"]) % len(colors)],
                            content=ft.Text(conv["name"][0].upper(), size=18, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            width=16, height=16, border_radius=8,
                            bgcolor=ft.Colors.GREEN_400,
                            right=0, bottom=0,
                            border=ft.border.all(2, BG_COLOR)
                        ) if conv["name"] in ["github", "reactjs"] else ft.Container()
                    ], width=50, height=50),
                    ft.Container(width=15),
                    ft.Column([
                        ft.Row([
                            styled_text(conv["name"], weight=ft.FontWeight.BOLD, size=16),
                            ft.Container(expand=True),
                            styled_text(conv["time"], size=12, color=ft.Colors.WHITE60)
                        ]),
                        ft.Container(height=5),
                        ft.Row([
                            styled_text(
                                conv["message"],
                                size=14,
                                color=ft.Colors.WHITE70 if conv["unread"] == 0 else TEXT_COLOR,
                                weight=ft.FontWeight.BOLD if conv["unread"] > 0 else None
                            ),
                            ft.Container(expand=True),
                            ft.Container(
                                content=ft.Text(str(conv["unread"]), size=12, color=TEXT_COLOR),
                                width=20, height=20, border_radius=10,
                                bgcolor=ACCENT_COLOR,
                                alignment=ft.alignment.center
                            ) if conv["unread"] > 0 else ft.Container()
                        ])
                    ], expand=True)
                ]),
                padding=ft.padding.symmetric(horizontal=15, vertical=12),
                on_click=lambda e: None  # Add navigation to chat
            )
        )

    return ft.Column([
        search_bar,
        ft.Container(
            content=styled_text("Messages", size=20, weight=ft.FontWeight.BOLD),
            padding=ft.padding.symmetric(horizontal=15, vertical=10)
        ),
        ft.Column(conversation_items, scroll=ft.ScrollMode.AUTO, expand=True)
    ], expand=True)

def create_profile_page(page):
    colors = [
        ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.PURPLE_400,
        ft.Colors.ORANGE_400, ft.Colors.PINK_400, ft.Colors.CYAN_400,
        ft.Colors.INDIGO_400, ft.Colors.TEAL_400
    ]

    # Profile stats
    posts_count = len([p for p in range(24)])  # Mock posts count
    followers_count = "1,234"
    following_count = "567"

    return ft.Column([
        # Profile Header
        ft.Container(
            content=ft.Column([
                # Profile info row
                ft.Row([
                    ft.Container(
                        width=90, height=90, border_radius=45,
                        bgcolor=ft.Colors.ORANGE_400, alignment=ft.alignment.center,
                        content=ft.Text("You", size=24, color=TEXT_COLOR, weight=ft.FontWeight.BOLD),
                        border=ft.border.all(3, ft.Colors.ORANGE_300)
                    ),
                    ft.Container(width=30),
                    ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text(str(posts_count), size=20, weight=ft.FontWeight.BOLD, color=TEXT_COLOR, text_align=ft.TextAlign.CENTER),
                                ft.Text("Posts", size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Container(width=25),
                            ft.Column([
                                ft.Text(followers_count, size=20, weight=ft.FontWeight.BOLD, color=TEXT_COLOR, text_align=ft.TextAlign.CENTER),
                                ft.Text("Followers", size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Container(width=25),
                            ft.Column([
                                ft.Text(following_count, size=20, weight=ft.FontWeight.BOLD, color=TEXT_COLOR, text_align=ft.TextAlign.CENTER),
                                ft.Text("Following", size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                        ])
                    ], expand=True)
                ]),
                ft.Container(height=20),

                # Bio section
                ft.Column([
                    ft.Text("Full Stack Developer", size=16, weight=ft.FontWeight.BOLD, color=TEXT_COLOR),
                    ft.Container(height=5),
                    ft.Text("🐍 Python | ⚛️ React | 🚀 Node.js", size=14, color=ft.Colors.WHITE70),
                    ft.Text("Building the future, one commit at a time 💻", size=14, color=ft.Colors.WHITE70),
                    ft.Container(height=5),
                    ft.Text("📍 San Francisco, CA", size=14, color=ft.Colors.WHITE60),
                    ft.Text("🔗 portfolio.dev", size=14, color=PRIMARY_COLOR),
                ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),

                ft.Container(height=20),

                # Action buttons
                ft.Row([
                    ft.ElevatedButton(
                        "Edit Profile",
                        bgcolor=DARK_GRAY,
                        color=TEXT_COLOR,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8)
                        ),
                        expand=True
                    ),
                    ft.Container(width=10),
                    ft.ElevatedButton(
                        "Share Profile",
                        bgcolor=DARK_GRAY,
                        color=TEXT_COLOR,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8)
                        ),
                        expand=True
                    ),
                    ft.Container(width=10),
                    ft.IconButton(
                        icon=ft.Icons.PERSON_ADD,
                        icon_color=TEXT_COLOR,
                        bgcolor=DARK_GRAY,
                        icon_size=20
                    )
                ])
            ]),
            padding=ft.padding.all(20)
        ),

        # Story highlights
        ft.Container(
            content=ft.Column([
                ft.Row([
                    styled_text("Story Highlights", size=16, weight=ft.FontWeight.BOLD),
                ]),
                ft.Container(height=10),
                ft.Row([
                    ft.Column([
                        ft.Container(
                            width=65, height=65, border_radius=32.5,
                            bgcolor=ft.Colors.PURPLE_400,
                            content=ft.Text("📱", size=25),
                            alignment=ft.alignment.center,
                            border=ft.border.all(2, DARK_GRAY)
                        ),
                        ft.Container(height=5),
                        styled_text("Apps", size=12)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Container(width=15),
                    ft.Column([
                        ft.Container(
                            width=65, height=65, border_radius=32.5,
                            bgcolor=ft.Colors.GREEN_400,
                            content=ft.Text("🎨", size=25),
                            alignment=ft.alignment.center,
                            border=ft.border.all(2, DARK_GRAY)
                        ),
                        ft.Container(height=5),
                        styled_text("Design", size=12)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Container(width=15),
                    ft.Column([
                        ft.Container(
                            width=65, height=65, border_radius=32.5,
                            bgcolor=ft.Colors.BLUE_400,
                            content=ft.Text("🚀", size=25),
                            alignment=ft.alignment.center,
                            border=ft.border.all(2, DARK_GRAY)
                        ),
                        ft.Container(height=5),
                        styled_text("Projects", size=12)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ])
            ]),
            padding=ft.padding.symmetric(horizontal=20, vertical=15)
        ),

        # Tab selector
        ft.Container(
            content=ft.Row([
                ft.IconButton(icon=ft.Icons.GRID_ON, icon_color=TEXT_COLOR, icon_size=28),
                ft.IconButton(icon=ft.Icons.PERSON_PIN_OUTLINED, icon_color=ft.Colors.WHITE60, icon_size=28),
            ], alignment=ft.MainAxisAlignment.CENTER),
            border=ft.border.only(top=ft.BorderSide(1, DARK_GRAY))
        ),

        # Posts Grid with more realistic content
        ft.Container(
            content=ft.GridView([
                ft.Container(
                    width=120, height=120,
                    bgcolor=colors[i % len(colors)],
                    border_radius=4,
                    content=ft.Stack([
                        ft.Text(
                            ["📱", "💻", "🔥", "⚡", "🚀", "🎨", "🌟", "💡", "🎯", "✨"][i % 10],
                            size=30
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.FAVORITE, color=TEXT_COLOR, size=16),
                                ft.Text(f"{random.randint(10, 999)}", size=12, color=TEXT_COLOR)
                            ]),
                            right=5, bottom=5,
                            bgcolor=ft.Colors.with_opacity(0.7, BG_COLOR),
                            padding=ft.padding.symmetric(horizontal=6, vertical=2),
                            border_radius=12
                        )
                    ]),
                    alignment=ft.alignment.center
                ) for i in range(24)
            ], runs_count=3, max_extent=120, child_aspect_ratio=1, spacing=2, run_spacing=2),
            expand=True,
            padding=ft.padding.symmetric(horizontal=5)
        )
    ], expand=True, scroll=ft.ScrollMode.AUTO)

def get_appbar_actions(current_tab):
    if current_tab == 0:  # Home
        return [
            ft.IconButton(
                icon=ft.Icons.ADD_BOX_OUTLINED,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Create Post"
            ),
            ft.IconButton(
                icon=ft.Icons.FAVORITE_BORDER,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Activity",
                badge=ft.Badge(
                    bgcolor=ACCENT_COLOR,
                    small_size=8,
                    text="5"
                )
            ),
            ft.IconButton(
                icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Direct Messages",
                badge=ft.Badge(
                    bgcolor=ACCENT_COLOR,
                    small_size=8,
                    text="12"
                )
            )
        ]
    elif current_tab == 1:  # Search
        return [
            ft.IconButton(
                icon=ft.Icons.QR_CODE_SCANNER,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Scan QR Code"
            )
        ]
    elif current_tab == 2:  # Reels
        return [
            ft.IconButton(
                icon=ft.Icons.VIDEOCAM,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Create Reel"
            )
        ]
    elif current_tab == 3:  # Messages
        return [
            ft.IconButton(
                icon=ft.Icons.VIDEO_CALL,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Video Call"
            ),
            ft.IconButton(
                icon=ft.Icons.EDIT,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="New Message"
            )
        ]
    else:  # Profile
        return [
            ft.IconButton(
                icon=ft.Icons.ADD_BOX_OUTLINED,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Create Post"
            ),
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_color=TEXT_COLOR,
                icon_size=28,
                tooltip="Menu"
            )
        ]

def instagram_home_view(page: ft.Page):
    """
    Enhanced Instagram home view function that returns a ft.View
    Compatible with your routing system
    """

    # Get tab titles for AppBar
    tab_titles = ["Instagram", "Search", "Reels", "Messages", "Profile"]

    # Create content based on current tab
    if app_state.current_tab == 0:
        content = create_home_feed(page)
    elif app_state.current_tab == 1:
        content = create_search_page(page)
    elif app_state.current_tab == 2:
        content = create_reels_page(page)
    elif app_state.current_tab == 3:
        content = create_messages_page(page)
    else:
        content = create_profile_page(page)

    # Enhanced AppBar with context-specific actions
    app_bar = ft.AppBar(
        title=ft.Text(
            tab_titles[app_state.current_tab],
            size=24,
            color=TEXT_COLOR,
            weight=ft.FontWeight.BOLD,
            font_family="cursive" if app_state.current_tab == 0 else None
        ),
        bgcolor=BG_COLOR,
        elevation=0,
        actions=get_appbar_actions(app_state.current_tab),
        leading=ft.IconButton(
            icon=ft.Icons.CAMERA_ALT_OUTLINED,
            icon_color=TEXT_COLOR,
            icon_size=28,
            tooltip="Camera"
        ) if app_state.current_tab == 0 else None,
        center_title=False if app_state.current_tab == 0 else True,
        toolbar_height=60
    )

    # Cupertino Bottom Navigation with enhanced styling
    cupertino_nav = ft.CupertinoNavigationBar(
        bgcolor=BG_COLOR,
        active_color=TEXT_COLOR,
        inactive_color=ft.Colors.WHITE60,
        icon_size=28,
        selected_index=app_state.current_tab,
        on_change=lambda e: on_tab_change(e, page),
        border=ft.Border(
            top=ft.BorderSide(1, DARK_GRAY)
        ),
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Home"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SEARCH_OUTLINED,
                selected_icon=ft.Icons.SEARCH,
                label="Search"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PLAY_CIRCLE_OUTLINE,
                selected_icon=ft.Icons.PLAY_CIRCLE,
                label="Reels"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                selected_icon=ft.Icons.CHAT_BUBBLE,
                label="Messages"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINE,
                selected_icon=ft.Icons.PERSON,
                label="Profile"
            )
        ]
    )

    # Return the enhanced main view with AppBar and Cupertino Navigation
    return ft.View(
        route="/instagram_home",
        appbar=app_bar,
        controls=[
            ft.Column([
                ft.Container(content=content, expand=True),
                cupertino_nav
            ], spacing=0, expand=True)
        ],
        scroll=ft.ScrollMode.HIDDEN,
        bgcolor=BG_COLOR,
        padding=ft.padding.all(0)
    )
