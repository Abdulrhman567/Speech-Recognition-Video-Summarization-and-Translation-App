from transformers import MarianMTModel, MarianTokenizer
import arabic_reshaper
import bidi.algorithm as bidi


class TranslationModel:
    def __init__(self, input_text) -> None:
        # Setting the translation model
        self.input_text = input_text
        self.model_name = "Helsinki-NLP/opus-mt-en-ar"
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

    def reshape_arabic_text(self, arabic_text):
        reshaped_text = arabic_reshaper.reshape(arabic_text)
        fully_reshaped_text = bidi.get_display(reshaped_text)
        return fully_reshaped_text

    def translate_text(self):
        # source_sentence = input("Enter an English sentence (or 'q' to quit): ")

        # Translate the input sentence
        inputs = self.tokenizer.encode(self.input_text, return_tensors="pt")
        translated = self.model.generate(
            inputs, max_length=1000, num_beams=4, early_stopping=True
        )
        translation = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        reshaped_translation_text = self.reshape_arabic_text(translation)

        # Display the translation
        print("Translation: ", reshaped_translation_text)
        return reshaped_translation_text


# max_length=128
# max_length=1500
