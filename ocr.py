import easyocr

reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext('captcha.png')
print(result)