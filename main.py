import customtkinter as ctk
from customtkinter import *
from tkinter.messagebox import showinfo
from PIL import Image
from frames.login import LoginFrame
from frames.register import RegisterFrame
from frames.speech_recognition import SpeechRecognitionFrame
from frames.summarization import SummarizationFrame
from frames.translation import TranslationFrame
from frames.VsT import VsFrame
import os

# WIDTH, HEIGHT = 950, 550
WIDTH, HEIGHT = 950, 600

# nltk.download("stopwords")
# nltk.download("punkt")

# with open("config.json") as data_file:
#     db_data = json.load(data_file)

# connection = None
# try:
#     # Connecting to the database
#     with psycopg2.connect(
#         host=db_data["host"],
#         dbname=db_data["database"],
#         user=db_data["username"],
#         password=db_data["password"],
#         port=db_data["port_num"],
#     ) as connection:
#         # Creating the cursor for the database to use the commands
#         with connection.cursor() as cur:
#             # excute db commands
#             cur.execute(
#                 """CREATE TABLE IF NOT EXISTS users(
#             id SERIAL PRIMARY KEY,
#             username VARCHAR(50) NOT NULL,
#             password VARCHAR(400) NOT NULL,
#             password_salt VARCHAR(50) NOT NULL
#             );"""
#             )
# cur.execute(
#     """INSERT INTO users (username, password, password_salt) VALUES (%s, %s, %s)""",
#     ("admin", "admin123", "admindoaifh"),
# )

# # Commiting changes
# connection.commit()

# # Closing the cursor and the connection to the database
# cur.close()
# connection.close()

# except Exception as error:
#     print(error)
# finally:
#     if connection:
#         connection.close()


class MainApp(ctk.CTk):
    def __init__(self, header="GET VsT", fg_color: str = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.loggedin_username = ""

        # Handle the main window
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.minsize(WIDTH, HEIGHT)
        self.maxsize(WIDTH, HEIGHT)
        self.config(padx=10, pady=10)
        self.title(f"{header}!")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Handle Configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Fonts
        self.btns_font = ctk.CTkFont(
            family="Arial",
            size=13,
            weight="bold",
        )

        # Loading images
        self.logo_image = ctk.CTkImage(
            Image.open(os.path.join("assets/images", "artificial-intelligence.png")),
            size=(32, 32),
        )
        self.home_image = ctk.CTkImage(
            light_image=Image.open(os.path.join("assets/images", "home_light.png")),
            # dark_image=Image.open(os.path.join("assets/images", "home_dark.png")),
            size=(22, 22),
        )
        self.speech_image = ctk.CTkImage(
            light_image=Image.open(os.path.join("assets/images", "microphone.png")),
            size=(22, 22),
        )
        self.summaize_image = ctk.CTkImage(
            Image.open(os.path.join("assets/images", "shopping-list.png")),
            size=(22, 22),
        )
        self.translate_image = ctk.CTkImage(
            Image.open(os.path.join("assets/images", "translate.png")), size=(24, 24)
        )
        self.icon_light_image = ctk.CTkImage(
            Image.open(os.path.join("assets/images", "image_icon_light.png")),
            size=(18, 18),
        )
        self.small_logo_image = ctk.CTkImage(
            Image.open(os.path.join("assets/images", "artificial-intelligence.png")),
            size=(22, 22),
        )

        # Frames
        self.navigation_frame = ctk.CTkFrame(
            master=self,
        )
        self.navigation_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        self.navigation_frame.grid_rowconfigure(
            6,
            weight=1,
        )

        # Handling naviagtion buttons and labels
        self.logo_label = ctk.CTkLabel(
            master=self.navigation_frame,
            text=f"  {header}",
            # text_color="#12b886",
            # text_color="#63e6be",
            text_color="#38d9a9",
            image=self.logo_image,
            compound="left",
            font=ctk.CTkFont(family="Arial", size=15, weight="bold"),
        )
        self.logo_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
        )
        # 343a40
        self.home_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="    Home",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            corner_radius=2,
            height=30,
            border_spacing=10,
            fg_color="transparent",
            text_color="#f1f3f5",
            hover=True,
            hover_color="#0ca678",
            image=self.home_image,
            anchor="w",
            command=self.display_home_frame,
        )
        self.home_btn.grid(
            row=1,
            column=0,
            sticky="ew",
        )

        self.speech_reco_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="Speech Reco",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            corner_radius=2,
            height=40,
            border_spacing=10,
            fg_color="transparent",
            text_color="#f1f3f5",
            hover=True,
            hover_color="#0ca678",
            image=self.speech_image,
            anchor="w",
            command=self.display_speech_recognition_frame,
        )
        self.speech_reco_btn.grid(
            row=2,
            column=0,
            sticky="ew",
        )

        self.summarize_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="Summarization",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            corner_radius=2,
            height=40,
            border_spacing=10,
            fg_color="transparent",
            text_color="#f1f3f5",
            hover=True,
            hover_color="#0ca678",
            image=self.summaize_image,
            anchor="w",
            command=self.display_summarization_frame,
        )
        self.summarize_btn.grid(
            row=3,
            column=0,
            sticky="ew",
        )

        self.translate_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="Translation",
            font=self.btns_font,
            corner_radius=2,
            height=40,
            border_spacing=10,
            fg_color="transparent",
            text_color="#f1f3f5",
            hover=True,
            hover_color="#0ca678",
            image=self.translate_image,
            anchor="w",
            command=self.display_translation_frame,
        )
        self.translate_btn.grid(
            row=4,
            column=0,
            sticky="ew",
        )

        self.vst_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="   Do VsT!",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            corner_radius=2,
            height=40,
            border_spacing=10,
            fg_color="transparent",
            text_color="#f1f3f5",
            hover=True,
            hover_color="#0ca678",
            image=self.small_logo_image,
            anchor="w",
            command=self.display_vs_frame,
        )
        self.vst_btn.grid(
            row=5,
            column=0,
            sticky="ew",
        )

        self.login_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="Login!",
            height=30,
            font=self.btns_font,
            text_color="#f1f3f5",
            hover=True,
            command=self.display_login_frame,
        )
        self.login_btn.grid(
            row=6,
            column=0,
            padx=10,
            # pady=(177, 0),
            pady=(135, 0),
            sticky="ew",
        )

        self.register_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="register!",
            height=30,
            font=self.btns_font,
            text_color="#f1f3f5",
            fg_color="#495057",
            hover=True,
            hover_color="#343a40",
            command=self.display_register_frame,
        )
        self.register_btn.grid(
            row=7,
            column=0,
            padx=10,
            pady=15,
            sticky="ew",
        )

        self.logout_btn = ctk.CTkButton(
            master=self.navigation_frame,
            text="Logout!",
            height=30,
            font=self.btns_font,
            text_color="#f1f3f5",
            fg_color="#495057",
            hover=True,
            hover_color="#343a40",
            command=self.logout_user,
        )
        self.logout_btn.grid(
            row=8,
            column=0,
            padx=10,
            pady=(0, 15),
            sticky="ew",
        )

        self.display_not_loggedin_frame()

    def update_login_status(self, username):
        self.loggedin_username = username
        self.display_home_frame()

    def check_login(self):
        if self.loggedin_username:
            return True
        return False

    def display_register_frame(self):
        # if not self.check_login():
        self.register_frame = RegisterFrame(
            self, update_login_status=self.update_login_status
        )
        self.register_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

    def display_login_frame(self):
        # if not self.check_login():
        self.login_frame = LoginFrame(
            self, update_login_status=self.update_login_status
        )
        self.login_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

    def logout_user(self):
        # if self.check_login():
        self.loggedin_username = ""
        showinfo(title="Logout!", message="You Have Loggedout Successfully!")
        self.display_not_loggedin_frame()

    # else:
    #     showwarning(title="Logout error!", message="Not loggedin yet!")

    def display_not_loggedin_frame(self):
        self.not_loggedin_frame = ctk.CTkFrame(
            master=self,
        )
        self.not_loggedin_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

        # frame configuration
        self.not_loggedin_frame.grid_rowconfigure(1, weight=1)
        self.not_loggedin_frame.grid_columnconfigure(1, weight=1)

        # Frame labels and buttons
        self.not_loggedin_label = ctk.CTkLabel(
            master=self.not_loggedin_frame,
            text="Not loggedin Yet!",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
        )
        self.not_loggedin_label.grid(
            row=0,
            column=0,
            columnspan=2,
            # padx=230,
            pady=150,
            sticky="nsew",
        )

        self.login_btn2 = ctk.CTkButton(
            master=self.not_loggedin_frame,
            text="Login!",
            width=200,
            height=30,
            font=self.btns_font,
            text_color="#f1f3f5",
            hover=True,
            command=self.display_login_frame,
        )
        self.login_btn2.grid(
            row=1,
            column=0,
            padx=90,
            pady=(0, 40),
            # sticky="ew",
        )

        self.register_btn2 = ctk.CTkButton(
            master=self.not_loggedin_frame,
            text="register!",
            width=200,
            height=30,
            font=self.btns_font,
            text_color="#f1f3f5",
            fg_color="#495057",
            hover=True,
            hover_color="#343a40",
            command=self.display_register_frame,
        )
        self.register_btn2.grid(
            row=1,
            column=1,
            padx=20,
            pady=(0, 40),
            # sticky="ew",
        )

    def display_home_frame(self):
        # Handling main frame buttons and labels
        # if self.check_login():
        self.home_frame = ctk.CTkFrame(
            master=self,
        )
        self.home_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

        # frame configuration
        self.home_frame.grid_columnconfigure(1, weight=0)

        self.no_model_label = ctk.CTkLabel(
            master=self.home_frame,
            text="No model choosen yet!",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
        )
        self.no_model_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=200,
            pady=(270, 0),
            # pady=230,
            sticky="nsew",
        )

        self.loggedin_as_label = ctk.CTkLabel(
            master=self.home_frame,
            text=f"Loggedin as: {self.loggedin_username}",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
        )
        self.loggedin_as_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=(240, 10),
            sticky="w",
        )

    def display_speech_recognition_frame(self):
        # if self.check_login():
        # Creating an instance of the Speech Recognition frame
        self.speech_recognition_frame = SpeechRecognitionFrame(self)
        self.speech_recognition_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

    # else:
    #     showwarning(
    #         title="Login required!", message="You need to be loggedin to go here."
    #     )

    def display_summarization_frame(self):
        # if self.check_login():
        # Creating an instance of the Summariaztion frame
        self.summarization_frame = SummarizationFrame(self)
        self.summarization_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

    # else:
    #     showwarning(
    #         title="Login required!", message="You need to be loggedin to go here."
    #     )

    def display_translation_frame(self):
        # if self.check_login():
        # Creating an instance of the Translation frame
        self.translation_frame = TranslationFrame(self)
        self.translation_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

    # else:
    #     showwarning(
    #         title="Login required!", message="You need to be loggedin to go here."
    #     )

    def display_vs_frame(self):
        # if self.check_login():
        self.vs_frame = VsFrame(self)
        self.vs_frame.grid(
            row=0,
            column=1,
            padx=(8, 0),
            sticky="nsew",
        )

    # else:
    #     showwarning(
    #         title="Login required!", message="You need to be loggedin to go here."
    #     )


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
