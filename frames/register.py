from typing import Optional, Tuple, Union
import customtkinter as ctk
from customtkinter import *
from tkinter.messagebox import showerror, showinfo
from PIL import Image
import psycopg2
import bcrypt

# from global_vars import HOST_NAME, DATEBASE_NAME, USERNAME, PASSWORD, PORT_NUM
import json
import os

# Loading Images and Fonts
register_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "login_modified.png")), size=(180, 180)
)

# Loading the configuration.json file data
with open("config.json") as data_file:
    db_data = json.load(data_file)


class RegisterFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        update_login_status,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )

        self.update_login_status = update_login_status

        # connection for the database
        # self.connection = None

        # Frame configuration
        self.grid_columnconfigure(0, weight=1)

        # Frame header, labels, entries and buttons
        self.header_image = ctk.CTkLabel(
            master=self,
            text="",
            image=register_image,
        )
        self.header_image.grid(
            row=0,
            column=0,
            pady=(60, 0),
            sticky="nsew",
        )

        self.username_label = ctk.CTkLabel(
            master=self,
            text="Enter Username:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
        )
        self.username_label.grid(
            row=1,
            column=0,
            padx=(0, 200),
            sticky="ew",
        )

        self.username_entry = ctk.CTkEntry(
            master=self,
            placeholder_text="username",
            width=300,
            height=30,
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14),
        )
        self.username_entry.grid(
            row=2,
            column=0,
            padx=(0, 30),
        )

        self.password_label = ctk.CTkLabel(
            master=self,
            text="Enter Password:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
        )
        self.password_label.grid(
            row=3,
            column=0,
            padx=(0, 200),
            pady=(10, 0),
            sticky="ew",
        )

        self.password_entry = ctk.CTkEntry(
            master=self,
            placeholder_text="password",
            width=300,
            height=30,
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14),
            show="*",
        )
        self.password_entry.grid(
            row=4,
            column=0,
            padx=(0, 30),
        )

        self.confirm_password_label = ctk.CTkLabel(
            master=self,
            text="Confirm Password:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
        )
        self.confirm_password_label.grid(
            row=5,
            column=0,
            padx=(20, 200),
            pady=(10, 0),
            sticky="ew",
        )

        self.confirm_password_entry = ctk.CTkEntry(
            master=self,
            placeholder_text="confirm password",
            width=300,
            height=30,
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14),
            show="*",
        )
        self.confirm_password_entry.grid(
            row=6,
            column=0,
            padx=(0, 30),
        )

        self.regiser_btn3 = ctk.CTkButton(
            master=self,
            text="register!",
            width=200,
            height=30,
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            text_color="#f1f3f5",
            hover=True,
            command=self.register_user,
        )
        self.regiser_btn3.grid(
            row=7,
            column=0,
            pady=30,
        )

    def add_user(self, username, hashed_password, salt):
        connection = None
        # Connect to the Postgresql database
        try:
            with psycopg2.connect(
                host=db_data["host"],
                dbname=db_data["database"],
                user=db_data["username"],
                password=db_data["password"],
                port=db_data["port_num"],
            ) as connection:
                with connection.cursor() as cur:
                    cur.execute(
                        """SELECT * FROM users WHERE username = %s""",
                        (username,),
                    )
                    existed_user = cur.fetchone()
                    if not existed_user:
                        self.username_entry.delete(0, "end")
                        self.password_entry.delete(0, "end")
                        self.confirm_password_entry.delete(0, "end")
                        cur.execute(
                            """INSERT INTO users (username, password, password_salt) VALUES (%s, %s, %s)""",
                            (
                                username,
                                hashed_password,
                                salt,
                            ),
                        )
                        showinfo(
                            title="Register Successfully!",
                            message="You registerd successfully, Welcome!.",
                        )
                        self.update_login_status(username)
                    else:
                        showerror(
                            title="User Exists!",
                            message="This username is already used try to use another username.",
                        )
        except Exception as error:
            print(error)
        finally:
            if connection:
                connection.close()

    def register_user(self):
        username_val = self.username_entry.get()
        password_val = self.password_entry.get()
        confirm_password_val = self.confirm_password_entry.get()
        if username_val and password_val and confirm_password_val:
            if password_val == confirm_password_val:
                # Salting and hashing the password after generating a salt of 16 bytes
                salt = bcrypt.gensalt(rounds=16)
                hashed_password = bcrypt.hashpw(
                    password_val.encode("utf-8"),
                    salt,
                )
                hashed_password = hashed_password.decode("utf-8")
                salt = salt.decode("utf-8")
                self.add_user(username_val, hashed_password, salt)
            else:
                showerror(
                    title="Matching Passwords!",
                    message="Password doesn't match, make sure you entered the passwords corrctly.",
                )
        else:
            showerror(
                title="Missing info!",
                message="Not all fields are filled, Please make sure to fill all the fields.",
            )
