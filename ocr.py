import easyocr
reader = easyocr.Reader(['en'])

def getCaptcha(url):
    result = reader.readtext(url)
    for (bbox, text, probability) in result:
        return(text.replace(" ", ""))