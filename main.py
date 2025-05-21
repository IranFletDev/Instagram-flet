import flet as ft
from flet import (
    AppBar, Column, Container, ElevatedButton, IconButton, Image, Icon,
    Page, Row, Text, TextField, icons, colors, border_radius, padding,
    ResponsiveRow, Card, Divider, ProgressRing, TextButton, Tabs, Tab,
    GridView, alignment, margin, ScrollMode, Stack
)
import base64
import io
from datetime import datetime
import random
import time

# Mock data for our Instagram clone
sample_users = [
    {"username": "travel_addict", "full_name": "Alex Traveler", "avatar": "https://picsum.photos/150/150?random=u1"},
    {"username": "foodie_gourmet", "full_name": "Jamie Foodie", "avatar": "https://picsum.photos/150/150?random=u2"},
    {"username": "fitness_guru", "full_name": "Sam Fitness", "avatar": "https://picsum.photos/150/150?random=u3"},
    {"username": "photo_master", "full_name": "Taylor Photos", "avatar": "https://picsum.photos/150/150?random=u4"},
    {"username": "fashion_icon", "full_name": "Morgan Style", "avatar": "https://picsum.photos/150/150?random=u5"},
]

sample_posts = [
    {
        "id": 1,
        "username": "travel_addict",
        "user_avatar": "https://picsum.photos/150/150?random=u1",
        "image_url": "https://picsum.photos/800/800?random=1",
        "caption": "Exploring the beautiful mountains today! The view was absolutely breathtaking. #nature #mountains #adventure",
        "likes": 342,
        "liked_by_me": False,
        "comments": [
            {"username": "photo_master", "text": "Wow! Amazing view! Where is this?"},
            {"username": "foodie_gourmet", "text": "Looks like paradise! 😍"},
            {"username": "fitness_guru", "text": "This inspires me to go hiking this weekend!"}
        ],
        "timestamp": "2 hours ago",
        "location": "Mountain Range, Colorado"
    },
    {
        "id": 2,
        "username": "foodie_gourmet",
        "user_avatar": "https://picsum.photos/150/150?random=u2",
        "image_url": "https://picsum.photos/800/800?random=2",
        "caption": "Made this delicious homemade pasta with fresh ingredients from the farmer's market. Recipe in bio! #foodporn #homemade #pasta",
        "likes": 528,
        "liked_by_me": False,
        "comments": [
            {"username": "travel_addict", "text": "Looks delicious! I need to try this recipe."},
            {"username": "fashion_icon", "text": "Your food always looks amazing! 👨‍🍳"},
            {"username": "photo_master", "text": "Great composition and lighting in this shot!"}
        ],
        "timestamp": "5 hours ago",
        "location": "Home Kitchen"
    },
    {
        "id": 3,
        "username": "fitness_guru",
        "user_avatar": "https://picsum.photos/150/150?random=u3",
        "image_url": "https://picsum.photos/800/800?random=3",
        "caption": "Morning workout complete! Starting the day with energy and positivity. #fitness #motivation #morningroutine",
        "likes": 476,
        "liked_by_me": False,
        "comments": [
            {"username": "travel_addict", "text": "You're such an inspiration!"},
            {"username": "fashion_icon", "text": "Love your workout outfit! Where is it from?"},
            {"username": "foodie_gourmet", "text": "What's your post-workout meal?"}
        ],
        "timestamp": "8 hours ago",
        "location": "Fitness Center"
    },
    {
        "id": 4,
        "username": "photo_master",
        "user_avatar": "https://picsum.photos/150/150?random=u4",
        "image_url": "https://picsum.photos/800/800?random=4",
        "caption": "Captured this perfect sunset at the beach yesterday. No filters needed for nature's beauty. #photography #sunset #beach",
        "likes": 892,
        "liked_by_me": False,
        "comments": [
            {"username": "travel_addict", "text": "The colors are incredible! What camera do you use?"},
            {"username": "fashion_icon", "text": "This would make a perfect wallpaper!"},
            {"username": "fitness_guru", "text": "Nothing beats a beach sunset! 🌅"}
        ],
        "timestamp": "1 day ago",
        "location": "Malibu Beach"
    },
    {
        "id": 5,
        "username": "fashion_icon",
        "user_avatar": "https://picsum.photos/150/150?random=u5",
        "image_url": "https://picsum.photos/800/800?random=5",
        "caption": "Today's OOTD for the fashion week. Mixing vintage and modern pieces for a unique look. #fashion #ootd #style",
        "likes": 723,
        "liked_by_me": False,
        "comments": [
            {"username": "photo_master", "text": "You always have the best style!"},
            {"username": "foodie_gourmet", "text": "Love the color combination!"},
            {"username": "travel_addict", "text": "Where did you get that amazing jacket?"}
        ],
        "timestamp": "1 day ago",
        "location": "Fashion Week, New York"
    }
]

sample_stories = [
    {"username": "travel_addict", "avatar": "https://picsum.photos/150/150?random=u1", "has_new": True},
    {"username": "foodie_gourmet", "avatar": "https://picsum.photos/150/150?random=u2", "has_new": True},
    {"username": "fitness_guru", "avatar": "https://picsum.photos/150/150?random=u3", "has_new": True},
    {"username": "photo_master", "avatar": "https://picsum.photos/150/150?random=u4", "has_new": False},
    {"username": "fashion_icon", "avatar": "https://picsum.photos/150/150?random=u5", "has_new": True},
    {"username": "tech_geek", "avatar": "https://picsum.photos/150/150?random=u6", "has_new": False},
    {"username": "music_lover", "avatar": "https://picsum.photos/150/150?random=u7", "has_new": True},
    {"username": "art_creator", "avatar": "https://picsum.photos/150/150?random=u8", "has_new": False},
]

explore_posts = [
    {"id": 101, "image_url": "https://picsum.photos/800/800?random=e1", "likes": 1245},
    {"id": 102, "image_url": "https://picsum.photos/800/800?random=e2", "likes": 876},
    {"id": 103, "image_url": "https://picsum.photos/800/800?random=e3", "likes": 2341},
    {"id": 104, "image_url": "https://picsum.photos/800/800?random=e4", "likes": 543},
    {"id": 105, "image_url": "https://picsum.photos/800/800?random=e5", "likes": 987},
    {"id": 106, "image_url": "https://picsum.photos/800/800?random=e6", "likes": 1532},
    {"id": 107, "image_url": "https://picsum.photos/800/800?random=e7", "likes": 765},
    {"id": 108, "image_url": "https://picsum.photos/800/800?random=e8", "likes": 2198},
    {"id": 109, "image_url": "https://picsum.photos/800/800?random=e9", "likes": 432},
    {"id": 110, "image_url": "https://picsum.photos/800/800?random=e10", "likes": 1876},
    {"id": 111, "image_url": "https://picsum.photos/800/800?random=e11", "likes": 954},
    {"id": 112, "image_url": "https://picsum.photos/800/800?random=e12", "likes": 2345},
]

class InstagramClone:
    def __init__(self):
        self.posts = sample_posts
        self.stories = sample_stories
        self.explore_posts = explore_posts
        self.users = sample_users
        self.current_user = {"username": "amirali_bj", "full_name": "Amirali Bahramjerdi", "avatar": "images/amirali.jpg"}
        self.current_view = "feed"
        self.upload_image_data = None
        self.is_loading = False
        self.screen_width = 0
        self.is_mobile = False
        self.is_tablet = False
        self.is_desktop = False
        
    def main(self, page: Page):
        page.fonts = {
            "Pacifico": "/fonts/Pacifico-Regular.ttf"
        }
        page.title = "IranFletDev Instagram"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 0
        page.bgcolor = colors.WHITE
        
        # Desktop View:
        # page.window_width = 1200
        # page.window_height = 800
        
        # Mobile View:
        page.window_width = 400 
        page.window_height = 812
        
        # Detect screen size and set responsive flags
        def page_resize(e):
            self.screen_width = page.window_width
            self.is_mobile = self.screen_width < 768
            self.is_tablet = 768 <= self.screen_width < 1200
            self.is_desktop = self.screen_width >= 1200
            self.update_responsive_layout()
            page.update()
            
        page.on_resize = page_resize
        
        # App components
        self.feed_view = Column(scroll=ScrollMode.AUTO, expand=True)
        self.explore_view = Column(scroll=ScrollMode.AUTO, expand=True)
        self.upload_view = Column(scroll=ScrollMode.AUTO, expand=True)
        self.activity_view = Column(scroll=ScrollMode.AUTO, expand=True)
        self.profile_view = Column(scroll=ScrollMode.AUTO, expand=True)
        self.story_view = Column(scroll=ScrollMode.AUTO, expand=True)
        
        # Loading indicator
        self.loading_indicator = Container(
            content=Column([
                ProgressRing(),
                Container(height=10),
                Text("Loading...", size=16)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=alignment.center,
            visible=False
        )
        
        # Navigation bar
        def nav_clicked(e):
            selected = e.control.data
            self.current_view = selected
            self.update_view(page)
            page.update()
            
        self.nav_bar = Row(
            [
                IconButton(
                    icon=icons.HOME,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Home",
                    data="feed",
                    on_click=nav_clicked
                ),
                IconButton(
                    icon=icons.SEARCH,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Explore",
                    data="explore",
                    on_click=nav_clicked
                ),
                IconButton(
                    icon=icons.ADD_BOX,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Upload",
                    data="upload",
                    on_click=nav_clicked
                ),
                IconButton(
                    icon=icons.FAVORITE_BORDER,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Activity",
                    data="activity",
                    on_click=nav_clicked
                ),
                IconButton(
                    icon=icons.PERSON,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Profile",
                    data="profile",
                    on_click=nav_clicked
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
        
        # Setup upload view
        caption_field = TextField(
            label="Write a caption...",
            multiline=True,
            min_lines=3,
            max_lines=5,
            border_radius=border_radius.all(10),
        )
        
        location_field = TextField(
            label="Add location",
            border_radius=border_radius.all(10),
        )
        
        upload_image_preview = Container(
            content=Column([
                Icon(icons.IMAGE, size=50, color=colors.GREY_400),
                Container(height=10),
                Text("No image selected", color=colors.GREY_600)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=400,
            height=400,
            bgcolor=colors.GREY_200,
            border_radius=border_radius.all(10),
            alignment=alignment.center
        )
        
        def simulate_loading(duration=2):
            self.is_loading = True
            self.loading_indicator.visible = True
            page.update()
            time.sleep(duration)
            self.is_loading = False
            self.loading_indicator.visible = False
            page.update()
        
        def handle_upload_click(e):
            # Simulate loading
            simulate_loading()
            
            # In a real app, this would save to a database
            if self.upload_image_data:
                new_post = {
                    "id": len(self.posts) + 1,
                    "username": self.current_user["username"],
                    "user_avatar": self.current_user["avatar"],
                    "image_url": f"https://picsum.photos/800/800?random={random.randint(100, 999)}",
                    "caption": caption_field.value,
                    "location": location_field.value,
                    "likes": 0,
                    "liked_by_me": False,
                    "comments": [],
                    "timestamp": "Just now"
                }
                self.posts.insert(0, new_post)
                caption_field.value = ""
                location_field.value = ""
                self.upload_image_data = None
                upload_image_preview.content = Column([
                    Icon(icons.IMAGE, size=50, color=colors.GREY_400),
                    Container(height=10),
                    Text("No image selected", color=colors.GREY_600)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                self.current_view = "feed"
                self.update_view(page)
                page.update()
        
        def pick_files_result(e: ft.FilePickerResultEvent):
            if e.files:
                # In a real app, we would process the actual file
                # Here we're just simulating it
                self.upload_image_data = "image_data"
                upload_image_preview.content = Image(
                    src=f"https://picsum.photos/800/800?random={random.randint(100, 999)}",
                    width=400,
                    height=400,
                    fit=ft.ImageFit.COVER,
                    border_radius=border_radius.all(10),
                )
                page.update()
        
        file_picker = ft.FilePicker(on_result=pick_files_result)
        page.overlay.append(file_picker)
        
        self.upload_view.controls = [
            Container(
                content=Text("Create New Post", size=20, weight=ft.FontWeight.BOLD),
                margin=margin.only(top=20, bottom=20),
                alignment=alignment.center
            ),
            Container(
                content=upload_image_preview,
                alignment=alignment.center,
                margin=margin.only(bottom=20)
            ),
            Container(
                content=ElevatedButton(
                    "Select from Gallery",
                    icon=icons.PHOTO_LIBRARY,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                ),
                alignment=alignment.center,
                margin=margin.only(bottom=10)
            ),
            Container(
                content=ElevatedButton(
                    "Take Photo",
                    icon=icons.CAMERA_ALT,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                ),
                alignment=alignment.center,
                margin=margin.only(bottom=20)
            ),
            Container(
                content=caption_field,
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(bottom=10)
            ),
            Container(
                content=location_field,
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(bottom=20)
            ),
            Container(
                content=Row([
                    Text("Tag People", weight=ft.FontWeight.BOLD),
                    Container(expand=True),
                    Icon(icons.ARROW_FORWARD_IOS, size=16, color=colors.GREY_600)
                ]),
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(bottom=10)
            ),
            Divider(height=1, color=colors.GREY_300),
            Container(
                content=Row([
                    Text("Also Post To", weight=ft.FontWeight.BOLD),
                    Container(expand=True),
                ]),
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(top=10, bottom=10)
            ),
            Container(
                content=Row([
                    Text("Facebook", weight=ft.FontWeight.W_500),
                    Container(expand=True),
                    ft.Switch(value=True)
                ]),
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(bottom=10)
            ),
            Container(
                content=Row([
                    Text("Twitter", weight=ft.FontWeight.W_500),
                    Container(expand=True),
                    ft.Switch(value=False)
                ]),
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(bottom=10)
            ),
            Container(
                content=Row([
                    Text("Tumblr", weight=ft.FontWeight.W_500),
                    Container(expand=True),
                    ft.Switch(value=False)
                ]),
                padding=padding.symmetric(horizontal=20),
                margin=margin.only(bottom=20)
            ),
            Container(
                content=ElevatedButton(
                    "Share",
                    style=ft.ButtonStyle(
                        color=colors.WHITE,
                        bgcolor=ft.colors.BLUE,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    width=200,
                    on_click=handle_upload_click
                ),
                alignment=alignment.center,
                margin=margin.only(top=10, bottom=20)
            )
        ]
        
        # Setup activity view
        self.activity_view.controls = [
            Container(
                content=Text("Activity", size=20, weight=ft.FontWeight.BOLD),
                margin=margin.only(top=20, bottom=20),
                alignment=alignment.center
            ),
            Container(
                content=Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        Tab(
                            text="Following",
                            content=Container(
                                content=Column([
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=user["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(user["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" liked your photo.", size=14)
                                                ]),
                                                Text("2h ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            Container(
                                                content=Image(
                                                    src=f"https://picsum.photos/100/100?random={i+20}",
                                                    width=40,
                                                    height=40,
                                                    fit=ft.ImageFit.COVER
                                                ),
                                            )
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    ) for i, user in enumerate(sample_users[:3])
                                ] + [
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=sample_users[3]["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(sample_users[3]["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" started following you.", size=14)
                                                ]),
                                                Text("5h ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            ElevatedButton(
                                                "Follow",
                                                style=ft.ButtonStyle(
                                                    color=colors.WHITE,
                                                    bgcolor=colors.BLUE,
                                                    shape=ft.RoundedRectangleBorder(radius=5),
                                                ),
                                            )
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    ),
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=sample_users[4]["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(sample_users[4]["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" commented: \"This is amazing!\"", size=14)
                                                ]),
                                                Text("1d ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            Container(
                                                content=Image(
                                                    src=f"https://picsum.photos/100/100?random=25",
                                                    width=40,
                                                    height=40,
                                                    fit=ft.ImageFit.COVER
                                                ),
                                            )
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    )
                                ]),
                                padding=padding.all(10)
                            )
                        ),
                        Tab(
                            text="You",
                            content=Container(
                                content=Column([
                                    Container(
                                        content=Text("Today", weight=ft.FontWeight.BOLD, size=16),
                                        margin=margin.only(top=10, bottom=10),
                                        padding=padding.only(left=10)
                                    ),
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=sample_users[0]["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(sample_users[0]["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" liked your photo.", size=14)
                                                ]),
                                                Text("2h ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            Container(
                                                content=Image(
                                                    src=f"https://picsum.photos/100/100?random=30",
                                                    width=40,
                                                    height=40,
                                                    fit=ft.ImageFit.COVER
                                                ),
                                            )
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    ),
                                    Container(
                                        content=Text("This Week", weight=ft.FontWeight.BOLD, size=16),
                                        margin=margin.only(top=10, bottom=10),
                                        padding=padding.only(left=10)
                                    ),
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=sample_users[1]["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(sample_users[1]["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" started following you.", size=14)
                                                ]),
                                                Text("2d ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            ElevatedButton(
                                                "Follow",
                                                style=ft.ButtonStyle(
                                                    color=colors.WHITE,
                                                    bgcolor=colors.BLUE,
                                                    shape=ft.RoundedRectangleBorder(radius=5),
                                                ),
                                            )
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    ),
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=sample_users[2]["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(sample_users[2]["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" commented on your post.", size=14)
                                                ]),
                                                Text("3d ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            Container(
                                                content=Image(
                                                    src=f"https://picsum.photos/100/100?random=31",
                                                    width=40,
                                                    height=40,
                                                    fit=ft.ImageFit.COVER
                                                ),
                                            )
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    ),
                                    Container(
                                        content=Text("This Month", weight=ft.FontWeight.BOLD, size=16),
                                        margin=margin.only(top=10, bottom=10),
                                        padding=padding.only(left=10)
                                    ),
                                    Container(
                                        content=Row([
                                            Container(
                                                content=Image(
                                                    src=sample_users[3]["avatar"],
                                                    width=40,
                                                    height=40,
                                                    border_radius=border_radius.all(20),
                                                    fit=ft.ImageFit.COVER
                                                ),
                                                margin=margin.only(right=10)
                                            ),
                                            Column([
                                                Row([
                                                    Text(sample_users[3]["username"], weight=ft.FontWeight.BOLD),
                                                    Text(" liked 3 of your photos.", size=14)
                                                ]),
                                                Text("2w ago", size=12, color=colors.GREY_600)
                                            ], spacing=5),
                                            Container(expand=True),
                                            Row([
                                                Container(
                                                    content=Image(
                                                        src=f"https://picsum.photos/100/100?random=32",
                                                        width=30,
                                                        height=30,
                                                        fit=ft.ImageFit.COVER
                                                    ),
                                                    margin=margin.only(right=5)
                                                ),
                                                Container(
                                                    content=Image(
                                                        src=f"https://picsum.photos/100/100?random=33",
                                                        width=30,
                                                        height=30,
                                                        fit=ft.ImageFit.COVER
                                                    ),
                                                    margin=margin.only(right=5)
                                                ),
                                                Container(
                                                    content=Image(
                                                        src=f"https://picsum.photos/100/100?random=34",
                                                        width=30,
                                                        height=30,
                                                        fit=ft.ImageFit.COVER
                                                    ),
                                                )
                                            ])
                                        ]),
                                        padding=padding.all(10),
                                        margin=margin.only(bottom=5)
                                    )
                                ]),
                                padding=padding.all(10)
                            )
                        )
                    ],
                    width=400
                ),
                alignment=alignment.center
            )
        ]
        
        # Setup profile view
        self.profile_tabs = Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    icon=icons.GRID_ON,
                    content=Container(
                        content=GridView(
                            runs_count=3,
                            max_extent=150,
                            child_aspect_ratio=1.0,
                            spacing=2,
                            run_spacing=2,
                            padding=padding.all(0),
                            controls=[
                                Container(
                                    content=Image(
                                        src=post["image_url"],
                                        fit=ft.ImageFit.COVER,
                                        width=150,
                                        height=150
                                    ),
                                ) for post in self.posts
                            ]
                        ),
                        padding=padding.all(0)
                    )
                ),
                Tab(
                    icon=icons.VIDEO_LIBRARY,
                    content=Container(
                        content=Column([
                            Container(
                                content=Text("No Reels Yet", size=20, weight=ft.FontWeight.BOLD),
                                alignment=alignment.center,
                                margin=margin.only(top=50)
                            ),
                            Container(
                                content=Text("Reels you create will appear here.", size=16, color=colors.GREY_600),
                                alignment=alignment.center,
                                margin=margin.only(top=10)
                            ),
                            Container(
                                content=ElevatedButton(
                                    "Create a Reel",
                                    style=ft.ButtonStyle(
                                        color=colors.WHITE,
                                        bgcolor=colors.BLUE,
                                        shape=ft.RoundedRectangleBorder(radius=5),
                                    ),
                                ),
                                alignment=alignment.center,
                                margin=margin.only(top=20)
                            )
                        ]),
                        padding=padding.all(20)
                    )
                ),
                Tab(
                    icon=icons.BOOKMARK_BORDER,
                    content=Container(
                        content=Column([
                            Container(
                                content=Text("Only you can see what you've saved", size=20, weight=ft.FontWeight.BOLD),
                                alignment=alignment.center,
                                margin=margin.only(top=50)
                            ),
                            Container(
                                content=Text("When you save something, it will appear here for you to easily find later.", 
                                            size=16, color=colors.GREY_600, text_align=ft.TextAlign.CENTER),
                                alignment=alignment.center,
                                margin=margin.only(top=10),
                                width=300
                            )
                        ]),
                        padding=padding.all(20)
                    )
                ),
                Tab(
                    icon=icons.PERSON_PIN,
                    content=Container(
                        content=Column([
                            Container(
                                content=Text("Photos and Videos of You", size=20, weight=ft.FontWeight.BOLD),
                                alignment=alignment.center,
                                margin=margin.only(top=50)
                            ),
                            Container(
                                content=Text("When people tag you in photos and videos, they'll appear here.", 
                                            size=16, color=colors.GREY_600, text_align=ft.TextAlign.CENTER),
                                alignment=alignment.center,
                                margin=margin.only(top=10),
                                width=300
                            )
                        ]),
                        padding=padding.all(20)
                    )
                ),
            ],
        )
        
        # Setup explore view
        self.explore_view.controls = [
            Container(
                content=TextField(
                    prefix_icon=icons.SEARCH,
                    hint_text="Search",
                    border_radius=border_radius.all(10),
                    filled=True,
                    bgcolor=colors.GREY_200,
                    height=40,
                    content_padding=padding.only(left=10, top=0, right=10, bottom=0)
                ),
                padding=padding.all(10),
                margin=margin.only(bottom=10)
            ),
            Container(
                content=GridView(
                    runs_count=3,
                    max_extent=150,
                    child_aspect_ratio=1.0,
                    spacing=2,
                    run_spacing=2,
                    padding=padding.all(0),
                    controls=[
                        Container(
                            content=Stack([
                                Image(
                                    src=post["image_url"],
                                    fit=ft.ImageFit.COVER,
                                    width=150,
                                    height=150
                                ),
                                Container(
                                    content=Row([
                                        Icon(icons.FAVORITE, color=colors.WHITE, size=14),
                                        Container(width=5),
                                        Text(str(post["likes"]), color=colors.WHITE, size=14, weight=ft.FontWeight.BOLD)
                                    ]),
                                    alignment=alignment.bottom_right,
                                    padding=padding.all(5)
                                )
                            ])
                        ) for post in self.explore_posts
                    ]
                ),
                padding=padding.all(0)
            )
        ]
        
        # Main layout
        self.app_bar = AppBar(
            title=Text("Instagram", size=24,font_family="Pacifico"),
            center_title=False,
            bgcolor=colors.WHITE,
            color=colors.BLACK,
            actions=[
                IconButton(
                    icon=icons.ADD_BOX_OUTLINED,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="New Post",
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="upload"))
                ),
                IconButton(
                    icon=icons.FAVORITE_BORDER,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Activity",
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="activity"))
                ),
                IconButton(
                    icon=icons.SEND,
                    icon_color=colors.BLACK,
                    icon_size=24,
                    tooltip="Direct Messages",
                    on_click=lambda _: print("Messages clicked")
                ),
            ]
        )
        
        # Desktop sidebar for larger screens
        self.desktop_sidebar = Container(
            content=Column([
                Container(
                    content=Text("Instagram", size=24, font_family="Pacifico"),
                    margin=margin.only(top=20, bottom=30, left=20)
                ),
                Container(
                    content=Row([
                        Icon(icons.HOME, size=24),
                        Container(width=10),
                        Text("Home", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="feed"))
                ),
                Container(
                    content=Row([
                        Icon(icons.SEARCH, size=24),
                        Container(width=10),
                        Text("Search", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="explore"))
                ),
                Container(
                    content=Row([
                        Icon(icons.EXPLORE, size=24),
                        Container(width=10),
                        Text("Explore", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="explore"))
                ),
                Container(
                    content=Row([
                        Icon(icons.VIDEO_LIBRARY, size=24),
                        Container(width=10),
                        Text("Reels", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: print("Reels clicked")
                ),
                Container(
                    content=Row([
                        Icon(icons.SEND, size=24),
                        Container(width=10),
                        Text("Messages", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: print("Messages clicked")
                ),
                Container(
                    content=Row([
                        Icon(icons.FAVORITE_BORDER, size=24),
                        Container(width=10),
                        Text("Notifications", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="activity"))
                ),
                Container(
                    content=Row([
                        Icon(icons.ADD_BOX_OUTLINED, size=24),
                        Container(width=10),
                        Text("Create", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="upload"))
                ),
                Container(
                    content=Row([
                        Container(
                            content=Image(
                                src=self.current_user["avatar"],
                                width=24,
                                height=24,
                                border_radius=border_radius.all(12),
                                fit=ft.ImageFit.COVER
                            ),
                        ),
                        Container(width=10),
                        Text("Profile", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=15, left=20),
                    on_click=lambda _: nav_clicked(ft.ControlEvent(None, data="profile"))
                ),
                Container(expand=True),
                Container(
                    content=Row([
                        Icon(icons.MENU, size=24),
                        Container(width=10),
                        Text("More", size=16, weight=ft.FontWeight.W_500)
                    ]),
                    margin=margin.only(bottom=20, left=20),
                    on_click=lambda _: print("More clicked")
                ),
            ], expand=True),
            width=220,
            bgcolor=colors.WHITE,
            border=ft.border.only(right=ft.border.BorderSide(1, colors.GREY_300)),
            visible=False  # Will be toggled based on screen size
        )
        
        # Main content area
        self.main_content = Container(
            content=Column([
                Container(
                    content=self.feed_view,
                    expand=True,
                    visible=True
                ),
                Container(
                    content=self.explore_view,
                    expand=True,
                    visible=False
                ),
                Container(
                    content=self.upload_view,
                    expand=True,
                    visible=False
                ),
                Container(
                    content=self.activity_view,
                    expand=True,
                    visible=False
                ),
                Container(
                    content=self.profile_view,
                    expand=True,
                    visible=False
                ),
                Container(
                    content=self.story_view,
                    expand=True,
                    visible=False
                ),
                Container(
                    content=self.nav_bar,
                    padding=padding.all(10),
                    border=ft.border.only(top=ft.border.BorderSide(1, colors.GREY_300)),
                    visible=True  # Will be toggled based on screen size
                )
            ], expand=True),
            expand=True
        )
        
        # Responsive layout container
        self.responsive_layout = Row([
            self.desktop_sidebar,
            self.main_content
        ], expand=True)
        
        # Loading overlay
        self.loading_overlay = Container(
            content=self.loading_indicator,
            width=page.width,
            height=page.height,
            bgcolor=ft.colors.with_opacity(0.7, ft.colors.BLACK),
            visible=False
        )
        
        # Add everything to the page
        page.add(
            self.app_bar,
            self.responsive_layout,
            self.loading_overlay
        )
        
        # Initialize the feed and set responsive layout
        self.screen_width = page.window_width
        self.is_mobile = self.screen_width < 768
        self.is_tablet = 768 <= self.screen_width < 1200
        self.is_desktop = self.screen_width >= 1200
        self.update_responsive_layout()
        self.update_view(page)
    
    def update_responsive_layout(self):
        # Update layout based on screen size
        if self.is_desktop:
            self.desktop_sidebar.visible = True
            self.main_content.content.controls[-1].visible = False  # Hide bottom nav bar
            self.app_bar.visible = False
        else:
            self.desktop_sidebar.visible = False
            self.main_content.content.controls[-1].visible = True  # Show bottom nav bar
            self.app_bar.visible = True
    
    def update_view(self, page):
        # Hide all views first
        for view_container in self.main_content.content.controls[:-1]:  # Exclude nav bar
            view_container.visible = False
        
        # Show the selected view
        if self.current_view == "feed":
            self.main_content.content.controls[0].visible = True
            self.update_feed()
        elif self.current_view == "explore":
            self.main_content.content.controls[1].visible = True
        elif self.current_view == "upload":
            self.main_content.content.controls[2].visible = True
        elif self.current_view == "activity":
            self.main_content.content.controls[3].visible = True
        elif self.current_view == "profile":
            self.main_content.content.controls[4].visible = True
            self.update_profile()
        elif self.current_view == "story":
            self.main_content.content.controls[5].visible = True
            self.update_story()
        
        page.update()
    
    def update_feed(self):
        self.feed_view.controls.clear()
        
        # Stories row
        stories_row = Container(
            content=Row(
                [
                    Column([
                        Container(
                            content=Stack([
                                Container(
                                    content=Image(
                                        src=story["avatar"],
                                        width=60,
                                        height=60,
                                        border_radius=border_radius.all(30),
                                        fit=ft.ImageFit.COVER
                                    ),
                                    border=ft.border.all(2, colors.PINK if story["has_new"] else colors.GREY_400),
                                    border_radius=border_radius.all(32),
                                    padding=padding.all(2),
                                    width=66,
                                    height=66
                                ),
                                Container(
                                    content=Container(
                                        content=Icon(icons.ADD, color=colors.WHITE, size=15),
                                        bgcolor=colors.BLUE,
                                        width=20,
                                        height=20,
                                        border_radius=border_radius.all(10),
                                        border=ft.border.all(2, colors.WHITE)
                                    ),
                                    alignment=alignment.bottom_right,
                                    visible=story["username"] == "amirali_bj"
                                )
                            ]),
                            margin=margin.only(right=10)
                        ),
                        Container(
                            content=Text(
                                "Your Story" if story["username"] == "amirali_bj" else story["username"],
                                size=12,
                                text_align=ft.TextAlign.CENTER,
                                no_wrap=True,
                                max_lines=1,
                                width=70
                            ),
                            margin=margin.only(top=5)
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                    for story in [{"username": "amirali_bj", "avatar": self.current_user["avatar"], "has_new": False}] + self.stories
                ],
                scroll=ft.ScrollMode.AUTO
            ),
            margin=margin.only(bottom=10),
            padding=padding.all(10),
            bgcolor=colors.WHITE
        )
        
        self.feed_view.controls.append(stories_row)
        
        # Posts
        for post in self.posts:
            # Create a post card
            def create_like_handler(post_id):
                def handle_like(e):
                    for p in self.posts:
                        if p["id"] == post_id:
                            p["liked_by_me"] = not p["liked_by_me"]
                            if p["liked_by_me"]:
                                p["likes"] += 1
                            else:
                                p["likes"] -= 1
                            self.update_feed()
                            self.feed_view.update()
                return handle_like
            
            def create_bookmark_handler(post_id):
                def handle_bookmark(e):
                    # In a real app, this would save to user's bookmarks
                    e.control.icon = icons.BOOKMARK if e.control.icon == icons.BOOKMARK_BORDER else icons.BOOKMARK_BORDER
                    self.feed_view.update()
                return handle_bookmark
            
            def create_comment_handler(post_id):
                def handle_comment(e):
                    # In a real app, this would open a comment dialog
                    print(f"Comment on post {post_id}")
                return handle_comment
            
            def create_share_handler(post_id):
                def handle_share(e):
                    # In a real app, this would open a share dialog
                    print(f"Share post {post_id}")
                return handle_share
            
            post_card = Container(
                content=Column([
                    # Post header
                    Container(
                        content=Row([
                            Container(
                                content=Image(
                                    src=post["user_avatar"],
                                    width=32,
                                    height=32,
                                    border_radius=border_radius.all(16),
                                    fit=ft.ImageFit.COVER
                                ),
                                margin=margin.only(right=10)
                            ),
                            Column([
                                Text(post["username"], weight=ft.FontWeight.BOLD, size=14),
                                Text(post.get("location", ""), size=12) if post.get("location") else Container(height=0)
                            ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.START),
                            Container(expand=True),
                            IconButton(
                                icon=icons.MORE_HORIZ,
                                icon_color=colors.BLACK,
                                icon_size=20
                            )
                        ]),
                        padding=padding.only(left=10, right=10, top=10, bottom=5)
                    ),
                    # Post image
                    Container(
                        content=Image(
                            src=post["image_url"],
                            width=self.screen_width if self.is_mobile else min(600, self.screen_width - 40),
                            height=self.screen_width if self.is_mobile else min(600, self.screen_width - 40),
                            fit=ft.ImageFit.COVER
                        )
                    ),
                    # Post actions
                    Container(
                        content=Row([
                            IconButton(
                                icon=icons.FAVORITE if post["liked_by_me"] else icons.FAVORITE_BORDER,
                                icon_color=colors.RED if post["liked_by_me"] else colors.BLACK,
                                icon_size=24,
                                on_click=create_like_handler(post["id"])
                            ),
                            IconButton(
                                icon=icons.CHAT_BUBBLE_OUTLINE,
                                icon_color=colors.BLACK,
                                icon_size=24,
                                on_click=create_comment_handler(post["id"])
                            ),
                            IconButton(
                                icon=icons.SEND,
                                icon_color=colors.BLACK,
                                icon_size=24,
                                on_click=create_share_handler(post["id"])
                            ),
                            Container(expand=True),
                            IconButton(
                                icon=icons.BOOKMARK_BORDER,
                                icon_color=colors.BLACK,
                                icon_size=24,
                                on_click=create_bookmark_handler(post["id"])
                            )
                        ]),
                        padding=padding.only(left=5, right=5)
                    ),
                    # Likes
                    Container(
                        content=Text(f"{post['likes']} likes", weight=ft.FontWeight.BOLD, size=14),
                        padding=padding.only(left=10, right=10, bottom=5)
                    ),
                    # Caption
                    Container(
                        content=Row([
                            Text(post["username"], weight=ft.FontWeight.BOLD, size=14),
                            Container(width=5),
                            Text(post["caption"], expand=True, size=14)
                        ]),
                        padding=padding.only(left=10, right=10, bottom=5)
                    ),
                    # Comments
                    Container(
                        content=Text(f"View all {len(post['comments'])} comments", color=colors.GREY_600, size=14),
                        padding=padding.only(left=10, right=10, bottom=5),
                        on_click=create_comment_handler(post["id"])
                    ),
                    # Sample comment
                    Container(
                        content=Row([
                            Text(post["comments"][0]["username"] if post["comments"] else "", weight=ft.FontWeight.BOLD, size=14),
                            Container(width=5),
                            Text(post["comments"][0]["text"] if post["comments"] else "", size=14)
                        ]),
                        padding=padding.only(left=10, right=10, bottom=5),
                        visible=len(post["comments"]) > 0
                    ),
                    # Timestamp
                    Container(
                        content=Text(post["timestamp"], size=12, color=colors.GREY_600),
                        padding=padding.only(left=10, right=10, bottom=10)
                    ),
                    # Add comment
                    Container(
                        content=Row([
                            Container(
                                content=Image(
                                    src=self.current_user["avatar"],
                                    width=30,
                                    height=30,
                                    border_radius=border_radius.all(15),
                                    fit=ft.ImageFit.COVER
                                ),
                                margin=margin.only(right=10)
                            ),
                            Container(
                                content=TextField(
                                    hint_text="Add a comment...",
                                    border="none",
                                    height=40,
                                    content_padding=padding.only(top=0, bottom=0),
                                    text_size=14
                                ),
                                expand=True
                            ),
                            TextButton(
                                text="Post",
                                style=ft.ButtonStyle(
                                    color=colors.BLUE,
                                ),
                            )
                        ]),
                        padding=padding.only(left=10, right=10, bottom=10),
                        border=ft.border.only(top=ft.border.BorderSide(1, colors.GREY_300))
                    )
                ]),
                bgcolor=colors.WHITE,
                margin=margin.only(bottom=10)
            )
            
            self.feed_view.controls.append(post_card)
    
    def update_profile(self):
        self.profile_view.controls.clear()
        
        # Profile header
        profile_header = Container(
            content=Column([
                Container(
                    content=Row([
                        Container(
                            content=Image(
                                src=self.current_user["avatar"],
                                width=80,
                                height=80,
                                border_radius=border_radius.all(40),
                                fit=ft.ImageFit.COVER
                            ),
                            margin=margin.only(right=20)
                        ),
                        Column([
                            Text(self.current_user["username"], size=20, weight=ft.FontWeight.BOLD),
                            Row([
                                Column([
                                    Text(str(len(self.posts)), weight=ft.FontWeight.BOLD, size=16),
                                    Text("Posts", size=14)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                Container(width=20),
                                Column([
                                    Text("245", weight=ft.FontWeight.BOLD, size=16),
                                    Text("Followers", size=14)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                Container(width=20),
                                Column([
                                    Text("315", weight=ft.FontWeight.BOLD, size=16),
                                    Text("Following", size=14)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            ])
                        ], expand=True)
                    ]),
                    margin=margin.only(bottom=10)
                ),
                Container(
                    content=Text(self.current_user["full_name"], weight=ft.FontWeight.BOLD, size=14),
                    margin=margin.only(bottom=5)
                ),
                Container(
                    content=Text("Digital creator | Photography enthusiast | Travel lover", size=14),
                    margin=margin.only(bottom=5)
                ),
                Container(
                    content=Text("www.instagram.com", size=14, color=colors.BLUE),
                    margin=margin.only(bottom=15)
                ),
                Container(
                    content=Row([
                        Container(
                            content=ElevatedButton(
                                "Edit Profile",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                    bgcolor=colors.WHITE,
                                    color=colors.BLACK,
                                    side=ft.BorderSide(1, colors.GREY_400)
                                ),
                                expand=True
                            ),
                            expand=True,
                            margin=margin.only(right=5)
                        ),
                        Container(
                            content=ElevatedButton(
                                "Share Profile",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                    bgcolor=colors.WHITE,
                                    color=colors.BLACK,
                                    side=ft.BorderSide(1, colors.GREY_400)
                                ),
                                expand=True
                            ),
                            expand=True,
                            margin=margin.only(left=5)
                        ),
                        Container(
                            content=IconButton(
                                icon=icons.PERSON_ADD,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                    bgcolor=colors.WHITE,
                                    color=colors.BLACK,
                                    side=ft.BorderSide(1, colors.GREY_400)
                                ),
                            ),
                            margin=margin.only(left=5)
                        )
                    ]),
                    margin=margin.only(bottom=15)
                ),
                # Story highlights
                Container(
                    content=Column([
                        Container(
                            content=Row([
                                Text("Story Highlights", weight=ft.FontWeight.BOLD, size=14),
                                Container(expand=True),
                                IconButton(
                                    icon=icons.KEYBOARD_ARROW_DOWN,
                                    icon_size=16
                                )
                            ]),
                            margin=margin.only(bottom=5)
                        ),
                        Container(
                            content=Text("Keep your favorite stories on your profile", size=14),
                            margin=margin.only(bottom=10)
                        ),
                        Container(
                            content=Row([
                                Column([
                                    Container(
                                        content=Icon(icons.ADD, size=30, color=colors.BLACK),
                                        width=60,
                                        height=60,
                                        border_radius=border_radius.all(30),
                                        border=ft.border.all(1, colors.GREY_400),
                                        alignment=alignment.center
                                    ),
                                    Container(height=5),
                                    Text("New", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                Container(width=15),
                                Column([
                                    Container(
                                        content=Image(
                                            src="https://picsum.photos/150/150?random=h1",
                                            width=60,
                                            height=60,
                                            border_radius=border_radius.all(30),
                                            fit=ft.ImageFit.COVER
                                        ),
                                        border=ft.border.all(1, colors.GREY_400),
                                        border_radius=border_radius.all(30),
                                    ),
                                    Container(height=5),
                                    Text("Travel", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                Container(width=15),
                                Column([
                                    Container(
                                        content=Image(
                                            src="https://picsum.photos/150/150?random=h2",
                                            width=60,
                                            height=60,
                                            border_radius=border_radius.all(30),
                                            fit=ft.ImageFit.COVER
                                        ),
                                        border=ft.border.all(1, colors.GREY_400),
                                        border_radius=border_radius.all(30),
                                    ),
                                    Container(height=5),
                                    Text("Food", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                Container(width=15),
                                Column([
                                    Container(
                                        content=Image(
                                            src="https://picsum.photos/150/150?random=h3",
                                            width=60,
                                            height=60,
                                            border_radius=border_radius.all(30),
                                            fit=ft.ImageFit.COVER
                                        ),
                                        border=ft.border.all(1, colors.GREY_400),
                                        border_radius=border_radius.all(30),
                                    ),
                                    Container(height=5),
                                    Text("Nature", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            ], scroll=ft.ScrollMode.AUTO),
                            margin=margin.only(bottom=15)
                        )
                    ]),
                    visible=True
                )
            ]),
            padding=padding.all(15),
            bgcolor=colors.WHITE
        )
        
        self.profile_view.controls.append(profile_header)
        
        # Profile tabs
        self.profile_view.controls.append(self.profile_tabs)
    
    def update_story(self):
        self.story_view.controls.clear()
        
        # Simulate a story view
        story_index = 0
        
        current_story = self.stories[story_index]
        
        def next_story(e):
            nonlocal story_index
            story_index = (story_index + 1) % len(self.stories)
            self.update_story()
            self.story_view.update()
        
        def prev_story(e):
            nonlocal story_index
            story_index = (story_index - 1) % len(self.stories)
            self.update_story()
            self.story_view.update()
        
        def close_story(e):
            self.current_view = "feed"
            self.update_view(e.page)
        
        # Story progress indicators
        progress_indicators = Row([
            Container(
                expand=True,
                height=2,
                bgcolor=colors.WHITE if i <= story_index else colors.WHITE54,
                border_radius=border_radius.all(1),
                margin=margin.only(right=2 if i < len(self.stories) - 1 else 0)
            ) for i in range(len(self.stories))
        ])
        
        # Story header
        story_header = Container(
            content=Row([
                Container(
                    content=Image(
                        src=current_story["avatar"],
                        width=30,
                        height=30,
                        border_radius=border_radius.all(15),
                        fit=ft.ImageFit.COVER
                    ),
                    margin=margin.only(right=10)
                ),
                Text(current_story["username"], color=colors.WHITE, weight=ft.FontWeight.BOLD),
                Text(" • ", color=colors.WHITE),
                Text("1h ago", color=colors.WHITE),
                Container(expand=True),
                IconButton(
                    icon=icons.MORE_HORIZ,
                    icon_color=colors.WHITE,
                    icon_size=20
                ),
                IconButton(
                    icon=icons.CLOSE,
                    icon_color=colors.WHITE,
                    icon_size=20,
                    on_click=close_story
                )
            ]),
            padding=padding.only(left=10, right=10, top=5, bottom=5)
        )
        
        # Story content
        story_content = Stack([
            Image(
                src=f"https://picsum.photos/800/1600?random={story_index+50}",
                width=self.screen_width,
                height=self.screen_width * 2,
                fit=ft.ImageFit.COVER
            ),
            Container(
                content=Row([
                    Container(
                        width=self.screen_width / 2,
                        height=self.screen_width * 2,
                        on_click=prev_story
                    ),
                    Container(
                        width=self.screen_width / 2,
                        height=self.screen_width * 2,
                        on_click=next_story
                    )
                ]),
            ),
            Container(
                content=Column([
                    Container(
                        content=progress_indicators,
                        padding=padding.all(10)
                    ),
                    story_header
                ]),
                gradient=ft.LinearGradient(
                    begin=alignment.top_center,
                    end=alignment.center,
                    colors=[colors.BLACK54, colors.TRANSPARENT]
                )
            ),
            Container(
                content=Row([
                    Container(
                        content=TextField(
                            hint_text="Send message",
                            hint_style=ft.TextStyle(color=colors.WHITE70),
                            border_color=colors.WHITE,
                            border_width=1,
                            border_radius=border_radius.all(20),
                            text_style=ft.TextStyle(color=colors.WHITE),
                            content_padding=padding.only(left=15, right=15, top=10, bottom=10),
                            filled=True,
                            bgcolor=colors.BLACK26,
                            expand=True
                        ),
                        expand=True,
                        margin=margin.only(right=10)
                    ),
                    IconButton(
                        icon=icons.FAVORITE,
                        icon_color=colors.WHITE,
                        icon_size=24
                    ),
                    IconButton(
                        icon=icons.SEND,
                        icon_color=colors.WHITE,
                        icon_size=24
                    )
                ]),
                padding=padding.all(10),
                alignment=alignment.bottom_center
            )
        ])
        
        self.story_view.controls.append(story_content)

# Run the app
app = InstagramClone()

# default view:
ft.app(target=app.main)

# web view:
# ft.app(
#     target=app.main,
#     assets_dir="assets",
#     view=ft.WEB_BROWSER,
#     host="0.0.0.0",
#     port=8550
# )