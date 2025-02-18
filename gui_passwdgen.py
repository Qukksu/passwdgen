"""Copyright (C) <2025> <Evrotskii Artem>
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option)
any later version.
"""

# Import required modules
from cli_passwdgen import PasswordGenerator
from entropy_checker import PasswordEntropyChecker
import flet as ft

def main(page: ft.Page):
    # Define constants
    SOFT_PURPLE = "#9F7AEA"
    generator = PasswordGenerator()

    def setup_page():
        # Configure main window properties
        page.title = "Cryptilus"
        page.window_center_on_screen = True
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = "#1A1625"
        page.window_width = 450
        page.window_height = 600
        page.on_window_event = lambda e: page.window_destroy() if e.data == "close" else None

    def create_button(text, on_click):
        # Create styled button with consistent appearance
        return ft.ElevatedButton(
            text,
            on_click=on_click,
            color=SOFT_PURPLE,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )

    def show_generator():
        # Clear current page content
        page.clean()

        # Create password display field
        pwd_text = ft.TextField(
            read_only=True,
            width=300,
            bgcolor="#2D2438",
            color="white",
            border_color=SOFT_PURPLE,
            hint_text="Password will appear here ^-^",
            text_align=ft.TextAlign.CENTER,
            text_size=16
        )

        # Create length input field
        length_input = ft.TextField(
            width=100,
            bgcolor="#2D2438",
            color="white",
            border_color=SOFT_PURPLE,
            hint_text="Length",
            hint_style=ft.TextStyle(color="#808080"),
            value="12",
            text_align=ft.TextAlign.CENTER,
            keyboard_type=ft.KeyboardType.NUMBER
        )

        # Create entropy display field
        entropy_text = ft.TextField(
            read_only=True,
            width=300,
            bgcolor="#2D2438",
            color="white",
            border_color=SOFT_PURPLE,
            hint_text="Password entropy will appear here",
            text_align=ft.TextAlign.CENTER,
            text_size=16
        )

        def generate_pwd(_):
            try:
                length = int(length_input.value)
                if length > 0:
                    generated_pwd = generator.generate_password(length)
                    pwd_text.value = generated_pwd
                    pwd_text.width = max(300, length * 15)

                    # Calculate and display entropy
                    checker = PasswordEntropyChecker()
                    entropy = checker.calculate_entropy(generated_pwd)
                    entropy_text.value = f"Password Entropy: {entropy:.2f} bits"
                else:
                    length_input.value = "12"
                page.update()
            except ValueError:
                length_input.value = "12"
                page.update()
        # Create container with generator interface
        content = ft.Container(
            content=ft.Column(
                controls=[
                    pwd_text,
                    entropy_text,
                    length_input,
                    ft.Row(
                        controls=[
                            create_button("Generate", generate_pwd),
                            create_button("Back", lambda _: show_main_menu())
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=20,
            width=400,
            alignment=ft.alignment.center
        )
        page.add(content)

    def show_credits():
        # Display credits and license information
        page.clean()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Created by Qukksu", color=SOFT_PURPLE, size=20),
                    ft.Text("Copyright (C) 2025 Evrotskii Artem", color=SOFT_PURPLE, size=16),
                    ft.Text(
                        "This program is free software; you can redistribute it and/or modify "
                        "it under the terms of the GNU General Public License as published by "
                        "the Free Software Foundation; either version 2 of the License, or "
                        "(at your option) any later version.",
                        color=SOFT_PURPLE,
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                        width=400,
                        selectable=True,
                        max_lines=None
                    ),
                    create_button("Back", lambda _: show_main_menu())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    def show_main_menu():
        # Display main menu with title and navigation buttons
        page.clean()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Cryptilus", size=32, color=SOFT_PURPLE, weight=ft.FontWeight.BOLD),
                    create_button("Generate", lambda _: show_generator()),
                    create_button("Credits", lambda _: show_credits())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    # Initialize application
    setup_page()
    show_main_menu()

if __name__ == "__main__":
    # Launch the Flet application
    ft.app(target=main)
