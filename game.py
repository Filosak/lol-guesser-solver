import keyboard
from final import solver

# game settings
difficulty = "Hard"    # Easy / Medium / Hard
mode = "Normal"        # Normal / Time / Names / Items

# path setup
item_path = "projekt/item/"
images_path = "projekt/images/"
find_images_path = "projekt/find_images/"
passives_images_path = "projekt/passives_images/"

data_path = "projekt/data.json"
item_data_path = "projekt/item.json"

tesseract_path = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# game solver
game = solver(mode, difficulty, item_path, images_path, find_images_path, passives_images_path, data_path, item_data_path, tesseract_path)
game.setup()
game.click(game.play_pos)

# game solver loop
while True:
    game.run()

    if keyboard.is_pressed('esc'):
        break