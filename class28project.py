class ReverseString:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

s = ReverseString("Hello this is Python")
print(s.reverse_words())