import customtkinter as ctk
from customtkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showwarning
import speech_recognition as sr
from PIL import Image
from models.speech_recongnition_model import SpeechRecognitionModel
import os

# size=(500, 100)
# loading images
speech_reco_header_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "Speech_Recognition.png")), size=(450, 100)
)
choose_file_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "image_icon_light.png")), size=(20, 20)
)
play_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "play.png")), size=(20, 20)
)
# speech_recognition_image = ctk.CTkImage(
#     Image.open(os.path.join("assets/images", "microphone.png")), size=(20, 20)
# )


class SpeechRecognitionFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        header="Speech Recognition",
        width: int = 200,
        height: int = 200,
        corner_radius: int = None,
        border_width: int = None,
        bg_color: str = "transparent",
        fg_color: str = None,
        border_color: str = None,
        background_corner_colors: str = None,
        overwrite_preferred_drawing_method: str = None,
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

        self.grid_columnconfigure(1, weight=1)

        self.choosen_file_name = ""

        # self.speech_reco_header_label = ctk.CTkLabel(
        #     master=self,
        #     text=header,
        #     font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
        #     text_color="#f1f3f5",
        # )
        # self.speech_reco_header_label.pack(
        #     anchor=CENTER,
        # )

        # Handling the buttons and labels of the frame
        self.speech_reco_header = ctk.CTkLabel(
            master=self,
            text="",
            image=speech_reco_header_image,
        )
        self.speech_reco_header.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            columnspan=2,
        )

        self.file_name_label = ctk.CTkLabel(
            master=self,
            text=f"File Name: {self.choosen_file_name}",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
            text_color="#f1f3f5",
        )
        self.file_name_label.grid(
            row=1,
            column=0,
            pady=(80, 5),
            columnspan=2,
        )

        self.file_choosing_btn = ctk.CTkButton(
            master=self,
            text="choose file",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            fg_color="#495057",
            hover=True,
            hover_color="#343a40",
            image=choose_file_image,
            compound="right",
            command=self.choose_file,
        )
        self.file_choosing_btn.grid(
            row=2,
            column=0,
            pady=10,
            columnspan=2,
        )

        # Model run button
        self.run_speech_reco_btn = ctk.CTkButton(
            master=self,
            text="run speechrecognition!",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            height=30,
            width=50,
            hover=True,
            image=play_image,
            compound="left",
            command=self.run_speech_recognition_model,
        )
        self.run_speech_reco_btn.grid(
            row=3,
            column=0,
            pady=20,
            columnspan=2,
        )

        # Handling the model output answer
        self.answer_label = ctk.CTkLabel(
            master=self,
            text="Answer:",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )
        self.answer_label.grid(
            padx=(10, 0),
        )

        self.answer_textbox = ctk.CTkTextbox(
            master=self,
            width=600,
            height=192,
            # height=142,
            fg_color="#343a40",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=15),
            wrap="word",
            spacing2=10,
            # state="disabled",
        )
        self.answer_textbox.grid(
            padx=5,
            pady=5,
            sticky="nsew",
            columnspan=2,
        )

    def choose_file(self):
        self.choosen_file_name = askopenfilename(
            # defaultextension="*.wav",
            # filetypes=("Video file", "*.wav"),
        )
        self.base_file_name = os.path.basename(self.choosen_file_name)
        self.file_name_label.configure(text=f"File Name: {self.base_file_name}")

    # def transcribe_audio(self):
    #     recognizer = sr.Recognizer()
    #     audio = sr.AudioFile(self.choosen_file_name)
    #     with audio as source:
    #         audio_text = recognizer.record(source)
    #     # return recognizer.recognize_google(audio_text)
    #     print(recognizer.recognize_google(audio_text))
    #     return recognizer.recognize_google(audio_text)

    def run_speech_recognition_model(self):
        if self.choosen_file_name:
            # speech_reco_output = self.transcribe_audio()
            self.speech_recognition_model = SpeechRecognitionModel(
                self.choosen_file_name
            )
            speech_recognition_output = self.speech_recognition_model.transcribe_audio()
            self.answer_textbox.insert("0.0", speech_recognition_output)
        else:
            showerror(
                title="No file found!",
                message="No file was seleted, Please select a file before you continue!",
            )
