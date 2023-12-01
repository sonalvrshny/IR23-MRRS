from langdetect import detect
import spacy

class QueryProcessor:
    def __init__(self):
        self.nlp = None
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # Model not found. Download it.
            print("Downloading the English language model...")
            spacy.cli.download("en_core_web_sm")

    def detect_language(self, text):
        try:
            language = detect(text)
            return language
        except Exception as e:
            print(f"Error detecting language: {e}")
            return None

    def parse_query(self, text):
        doc = self.nlp(text)
        keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
        return keywords

# Example usage
if __name__ == "__main__":
    query_processor = QueryProcessor()

    user_query = "बटर नान बनाने की विधि|"

    # Language detection
    detected_language = query_processor.detect_language(user_query)
    print(f"Detected language: {detected_language}")

    # Query parsing
    parsed_keywords = query_processor.parse_query(user_query)
    print(f"Parsed keywords: {parsed_keywords}")
