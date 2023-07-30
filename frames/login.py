import customtkinter as ctk
from customtkinter import *
from tkinter.messagebox import showinfo, showerror
from PIL import Image
import psycopg2
import bcrypt
from global_vars import HOST_NAME, DATEBASE_NAME, USERNAME, PASSWORD, PORT_NUM
import json
import os

# Loading images and assets
login_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "login_pic.jpg")), size=(300, 150)
)
password_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "password.png")), size=(180, 180)
)
# size=(256, 256)

# Reading the configuration.json file
with open("config.json") as data_file:
    db_data = json.load(data_file)

# Getting the needed data for the DB connection
# host_name = os.environ.get("MYAPP_DB_HOST")
# port_num = os.environ.get("MY_APP_DB_PORTNUM")
# database = os.environ.get("MY_APP_DB_DBNAME")
# username = os.environ.get("MY_APP_DB_USERNAME")
# password = os.environ.get("MY_APP_DB_PASSWORD")


class LoginFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        update_login_status,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str = "transparent",
        fg_color: str = None,
        border_color: str = None,
        background_corner_colors: str = None,
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

        # Handling frame grid configuration
        self.grid_columnconfigure(0, weight=1)

        # Handling the labels and the buttons of the login frame
        self.header_image_label = ctk.CTkLabel(
            master=self,
            text="",
            image=password_image,
        )
        self.header_image_label.grid(
            row=0,
            column=0,
            pady=(80, 20)
            # pady=20,
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

        # Entries
        self.username_input = StringVar()
        self.username_entry = ctk.CTkEntry(
            master=self,
            placeholder_text="username",
            # textvariable=self.username_input,
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

        self.password_input = StringVar()
        self.password_entry = ctk.CTkEntry(
            master=self,
            # textvariable=self.password_input,
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

        self.login_btn3 = ctk.CTkButton(
            master=self,
            text="Loign!",
            width=200,
            height=30,
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            text_color="#f1f3f5",
            hover=True,
            command=self.login_user,
        )
        self.login_btn3.grid(
            row=5,
            column=0,
            pady=30,
        )

    def check_user_existance(self, username: str, password_val: str):
        connection = None
        # Connecting to the Postgressql database
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
                    if existed_user:
                        stored_hashed_password = existed_user[2]
                        stored_salt = existed_user[3]
                        # stored_salt = stored_salt.decode("utf-8")
                        # print(stored_salt)
                        # password_val = password_val.encode("utf-8")
                        new_hashed_password = bcrypt.hashpw(
                            password_val.encode("utf-8"),
                            stored_salt.encode("utf-8"),
                        )
                        new_hashed_password = new_hashed_password.decode("utf-8")
                        if new_hashed_password == stored_hashed_password:
                            self.username_entry.delete(0, "end")
                            self.password_entry.delete(0, "end")
                            showinfo(
                                title="Login Successfully!",
                                message="Loggedin successfully, welcome back!.",
                            )
                            self.update_login_status(username)
                        else:
                            showerror(
                                title="Login Failed!",
                                message="The password you entered is incorrect, Try again!.",
                            )
                    else:
                        showerror(
                            title="Not Found!",
                            message="The username you entered is incorrect or not found, Please try again!.",
                        )
        except Exception as error:
            print(error)
        finally:
            if connection:
                connection.close

    def login_user(self):
        username_val = self.username_entry.get()
        password_val = self.password_entry.get()
        if username_val and password_val:
            self.check_user_existance(username_val, password_val)
        else:
            showerror(
                title="Missing Info!",
                message="Not all fields are filled, Please make sure to fill all the fields.",
            )
