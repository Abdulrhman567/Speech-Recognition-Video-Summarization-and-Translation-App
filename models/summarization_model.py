from transformers import pipeline


class SummarizationModel:
    def __init__(self, text) -> None:
        self.text = text

    def summarize_text(self):
        summarizer = pipeline("summarization")
        # text = """
        # """
        summary_length = 200
        summary = summarizer(
            self.text, max_length=summary_length, min_length=70, do_sample=False
        )
        print(summary[0]["summary_text"])
        return summary[0]["summary_text"]


# summary_length = 50

# import nltk
# from collections import defaultdict
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize


# class SummarizationModel:
#     def __init__(self, text) -> None:
#         self.text = text
#         # self.ratio = 0.35
#         # self.ratio = 0.25
#         # self.ratio = 0.10
#         self.ratio = 0.20

#     def summarize_text(self, text="", ratio=0.35):
#         stop_words = set(nltk.corpus.stopwords.words("english"))
#         sentences = nltk.tokenize.sent_tokenize(self.text)

#         word_frequencies = defaultdict(int)
#         for i, sentence in enumerate(sentences):
#             words = nltk.tokenize.word_tokenize(sentence)
#             words = [word for word in words if word.lower() not in stop_words]
#             for word in words:
#                 word_frequencies[word] += 1

#         sentence_scores = defaultdict(int)
#         for i, sentence in enumerate(sentences):
#             words = nltk.tokenize.word_tokenize(sentence)
#             words = [word for word in words if word.lower() not in stop_words]
#             for word in words:
#                 sentence_scores[i] += word_frequencies[word]

#         summarized_text = " ".join(
#             [
#                 sentences[i]
#                 for i in sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
#                     : int(self.ratio * len(sentences))
#                 ]
#             ]
#         )

#         return summarized_text
