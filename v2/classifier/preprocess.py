import re

class PreProcess:

    def _transform(self, string):
        return string

    @staticmethod
    def transform(preprocess, string):
        return preprocess._transform(string)

    @staticmethod
    def chain_transform(preprocesses, strings):
        for preprocess in preprocesses:
            for idx, string in enumerate(strings):
                strings[idx] = preprocess._transform(string)

class Strip(PreProcess):
    def _transform(self, string):
            return string.strip()

class SingatureRemoval(PreProcess):
    def _transform(self, string):
        # TODO remove signature
        return string

class SearchAndReplaceUrl(PreProcess):

    def __init__(self):
        self.URL = "URL"
        self.regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def _transform(self, string):
        detected_strings = self.regex.findall(string)
        for detected_string in detected_strings:
            string = string.replace(detected_string, self.URL)
        return string

class RemovePunctuation(PreProcess):
    def _transform(self, string):
        # TODO remove punctuation
        pass

class RemoveQuestionMark(PreProcess):
    def _transform(self, string):
        return string.replace("?", "")

class AddAdditionalHWClause(PreProcess):
    def _transform(self, string):
        # TODO add verb for single Ws and Hs.
        pass
