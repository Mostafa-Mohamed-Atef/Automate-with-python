import pyshorteners
import pyperclip

s = pyshorteners.Shortener()
url = input("Enter url: \n")
shorter_url = s.tinyurl.short(url)
pyperclip.copy(shorter_url)
print(f"Output: {shorter_url} is copied on your clipboard")