def parse(text):
    text = text.lower()
    text = text.split()

    if text[0] == "exit":
        return "exit"

    else:
        return None
