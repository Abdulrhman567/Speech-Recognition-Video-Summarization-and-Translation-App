# from pyexpat import model
from typing import Optional, Tuple, Union
import customtkinter as ctk
from customtkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from PIL import Image
from models.speech_recongnition_model import SpeechRecognitionModel
from models.summarization_model import SummarizationModel
from models.translation_model import TranslationModel
import os

# Loading images and assets
large_logo_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "artificial-intelligence.png")),
    size=(46, 46),
)
play_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "play.png")), size=(20, 20)
)
speech_recognition_vst_img = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "microphone-vst.png")), size=(80, 80)
)
summariaztion_vst_img = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "contract.png")), size=(80, 80)
)
translation_vst_img = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "chat.png")), size=(90, 90)
)


class VsFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
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
            **kwargs,
        )

        # FONTS
        self.models_font = ctk.CTkFont(family="Arail", size=14, weight="bold")

        self.choosen_file_name = ""

        # Handling frame grid configuration
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Handling frame labels and buttons(widgets)
        self.header_image_label = ctk.CTkLabel(
            master=self,
            text="",
            image=large_logo_image,
        )
        self.header_image_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=(0, 170),
            pady=20,
            # sticky="nsew",
        )

        self.header_label = ctk.CTkLabel(
            master=self,
            text="Do VsT!",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=28, weight="bold"),
        )
        self.header_label.grid(
            row=0,
            column=0,
            # padx=(20, 0),
            pady=20,
        )

        self.speech_recognition_img_label = ctk.CTkLabel(
            master=self,
            text="",
            image=speech_recognition_vst_img,
        )
        self.speech_recognition_img_label.grid(
            row=1,
            column=0,
            # padx=(0, 400),
            padx=(50, 0),
            pady=(40, 20),
            sticky="w",
        )

        self.speech_recognition_text_label = ctk.CTkLabel(
            master=self,
            text="Speech Recognition",
            text_color="#20c997",
            font=self.models_font,
        )
        self.speech_recognition_text_label.grid(
            row=2,
            column=0,
            padx=(20, 0),
            # pady=(100, 0),
            sticky="w",
        )

        self.summarization_img_label = ctk.CTkLabel(
            master=self,
            text="",
            image=summariaztion_vst_img,
        )
        self.summarization_img_label.grid(
            row=1,
            column=0,
            # padx=(400, 0),
            # padx=(20, 0),
            pady=(40, 20),
        )

        self.summarization_text_label = ctk.CTkLabel(
            master=self,
            text="Summarization",
            text_color="#20c997",
            font=self.models_font,
        )
        self.summarization_text_label.grid(
            row=2,
            column=0,
            # padx=(20, 0),
        )

        self.translation_img_label = ctk.CTkLabel(
            master=self,
            text="",
            image=translation_vst_img,
        )
        self.translation_img_label.grid(
            row=1,
            column=0,
            # padx=(120, 0),
            padx=(0, 50),
            pady=(40, 20),
            sticky="e",
        )

        self.translation_text_label = ctk.CTkLabel(
            master=self,
            text="Translation",
            text_color="#20c997",
            font=self.models_font,
        )
        self.translation_text_label.grid(
            row=2,
            column=0,
            padx=(0, 60),
            sticky="e",
        )

        self.run_vst_btn = ctk.CTkButton(
            master=self,
            text="run video recognition-summerization",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            height=30,
            width=50,
            hover=True,
            image=play_image,
            compound="left",
            command=self.run_models,
        )
        self.run_vst_btn.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=(60, 40),
        )

        self.answer_label = ctk.CTkLabel(
            master=self,
            text="Answer:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )
        self.answer_label.grid(
            row=4,
            column=0,
            padx=10,
            sticky="w",
        )

        self.answer_textbox = ctk.CTkTextbox(
            master=self,
            width=800,
            height=156,
            # height=194,
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
            row=5,
            column=0,
            columnspan=2,
            padx=5,
        )

    def choose_file(self):
        self.choosen_file_name = askopenfilename()

    def run_models(self):
        self.choose_file()
        if self.choosen_file_name:
            self.speech_recognition_model = SpeechRecognitionModel(
                self.choosen_file_name
            )
            self.speech_reco_output = self.speech_recognition_model.transcribe_audio()
            if self.speech_reco_output:
                self.summarization_model = SummarizationModel(self.speech_reco_output)
                self.summaization_text_output = (
                    self.summarization_model.summarize_text()
                )
                if self.summaization_text_output:
                    self.translation_model = TranslationModel(
                        self.summaization_text_output
                    )
                    self.translation_text_output = (
                        self.translation_model.translate_text()
                    )
                    self.answer_textbox.insert("0.0", self.translation_text_output)
        else:
            showerror(
                title="Models interrupted!",
                message="One of the models did not function correct please try again.!",
            )
