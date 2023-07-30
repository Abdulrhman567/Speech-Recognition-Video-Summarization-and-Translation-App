import customtkinter as ctk
from customtkinter import *
from tkinter.messagebox import showerror
from PIL import Image
from models.translation_model import TranslationModel
import os

translation_header_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "Translation2.png")), size=(450, 100)
)
play_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "play.png")), size=(20, 20)
)


class TranslationFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int = None,
        border_width: int = None,
        bg_color: str = "transparent",
        fg_color: str = None,
        border_color: str = None,
        background_corner_colors: str = None,
        overwrite_preferred_drawing_method: str = None,
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

        self.grid_columnconfigure(1, weight=1)

        # self.translation_header_label = ctk.CTkLabel(
        #     master=self,
        #     text=header,
        #     font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
        #     text_color="#f1f3f5",
        # )
        # self.translation_header_label.pack(
        #     anchor=CENTER,
        # )
        self.translation_header = ctk.CTkLabel(
            master=self,
            text="",
            image=translation_header_image,
        )
        self.translation_header.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            columnspan=2,
        )

        # Handling the input
        self.enter_input_label = ctk.CTkLabel(
            master=self,
            text="Enter text to Translate:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )
        self.enter_input_label.grid(
            # row=0,
            # column=0,
            padx=10,
            pady=10,
        )

        self.enter_input_textbox = ctk.CTkTextbox(
            master=self,
            width=800,
            height=160,
            # height=140,
            fg_color="#343a40",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=15),
            wrap="word",
            spacing2=10,
        )
        self.enter_input_textbox.grid(
            padx=5,
            columnspan=2,
        )

        # Model Run button
        self.run_translation_btn = ctk.CTkButton(
            master=self,
            text="run translation!",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            hover=True,
            image=play_image,
            command=self.run_translation_model,
        )
        self.run_translation_btn.grid(
            pady=(20, 10),
            columnspan=2,
        )

        # Handling the model output
        self.answer_label = ctk.CTkLabel(
            master=self,
            text="Answer:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )
        self.answer_label.grid(
            padx=(0, 125),
            pady=(0, 5),
        )

        self.answer_textbox = ctk.CTkTextbox(
            master=self,
            width=800,
            height=158,
            # direction="rtl",
            # height=128,
            fg_color="#343a40",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=15),
            wrap="word",
            spacing2=10,
            # state="disabled",
        )
        self.answer_textbox.grid(
            padx=5,
            columnspan=2,
        )

        # self.answer_entry = ctk.Sco(
        #     master=self,
        #     width=800,
        #     height=158,
        #     justify="right",
        #     fg_color="#343a40",
        #     text_color="#f1f3f5",
        #     font=ctk.CTkFont(family="Arial", size=15),
        #     # bd=0,
        #     # highlightthickness=0,
        #     # wrap="word",
        #     # spacing2=10,
        # )
        # self.answer_entry.grid(
        #     padx=5,
        #     columnspan=2,
        # )

    def run_translation_model(self):
        self.input_text_to_translate = self.enter_input_textbox.get("0.0", "end")
        if self.input_text_to_translate:
            self.translation_model = TranslationModel(
                input_text=self.input_text_to_translate
            )
            translated_text = self.translation_model.translate_text()
            self.answer_textbox.tag_config("rtl", justify="right")
            self.answer_textbox.insert(END, translated_text)
        else:
            showerror(
                title="No Text Found!!",
                message="No text was found, Try to type some text before you continue.",
            )
