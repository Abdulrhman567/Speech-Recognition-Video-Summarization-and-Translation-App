import customtkinter as ctk
from customtkinter import *
from tkinter.messagebox import showerror
from PIL import Image
import nltk
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from models.summarization_model import SummarizationModel
import os

# Loading images
summarization_header_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "Summarization.png")), size=(450, 100)
)
play_image = ctk.CTkImage(
    Image.open(os.path.join("assets/images", "play.png")), size=(20, 20)
)


class SummarizationFrame(ctk.CTkFrame):
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

        # self.summarization_header_label = ctk.CTkLabel(
        #     master=self,
        #     text=header,
        #     font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
        #     text_color="#f1f3f5",
        # )
        # self.summarization_header_label.pack(
        #     anchor=CENTER,
        # )

        # Handling the header
        self.summarization_header = ctk.CTkLabel(
            master=self,
            text="",
            image=summarization_header_image,
        )
        self.summarization_header.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            columnspan=2,
        )

        # Handling the input
        self.enter_input_label = ctk.CTkLabel(
            master=self,
            text="Enter text to Summarize:",
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
        self.run_summarization_btn = ctk.CTkButton(
            master=self,
            text="run summarization!",
            text_color="#f1f3f5",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            hover=True,
            image=play_image,
            command=self.run_summarization_model,
        )
        self.run_summarization_btn.grid(
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
            # height=128
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

    # def summarize_text(self, text, ratio=0.35):
    #     stop_words = set(nltk.corpus.stopwords.words("english"))
    #     sentences = nltk.tokenize.sent_tokenize(text)

    #     word_frequencies = defaultdict(int)
    #     for i, sentence in enumerate(sentences):
    #         words = nltk.tokenize.word_tokenize(sentence)
    #         words = [word for word in words if word.lower() not in stop_words]
    #         for word in words:
    #             word_frequencies[word] += 1

    #     sentence_scores = defaultdict(int)
    #     for i, sentence in enumerate(sentences):
    #         words = nltk.tokenize.word_tokenize(sentence)
    #         words = [word for word in words if word.lower() not in stop_words]
    #         for word in words:
    #             sentence_scores[i] += word_frequencies[word]

    #     summarized_text = " ".join(
    #         [
    #             sentences[i]
    #             for i in sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
    #                 : int(ratio * len(sentences))
    #             ]
    #         ]
    #     )

    #     return summarized_text
    # return self.summarized_text(text)

    def run_summarization_model(self):
        get_input_text = self.enter_input_textbox.get("0.0", "end")
        if get_input_text:
            self.summarization_model = SummarizationModel(get_input_text)
            summarization_text_output = self.summarization_model.summarize_text()
            self.answer_textbox.insert("0.0", summarization_text_output)
            # output_text = self.summarize_text(text=get_input_text)
        else:
            showerror(
                title="No Text Found!!",
                message="No text was found, Try to type some text before you continue.",
            )
