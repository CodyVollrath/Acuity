from PIL import ImageGrab

def save_screenshot(file_loc: str):
    screenshot = ImageGrab.grab()
    screenshot.save(file_loc)
