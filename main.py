import glob
import os
import random
from PIL import Image

# Путь к директории с картинками
image_directory = "/path/to/html/img"

# Получаем список всех файлов с расширением .jpg, .jpeg, .png в директории
image_files = glob.glob(os.path.join(image_directory, "*.jpg")) + glob.glob(os.path.join(image_directory, "*.jpeg")) + glob.glob(os.path.join(image_directory, "*.png"))

# Выбираем случайную картинку из списка
random_image = random.choice(image_files)

# Открываем и отображаем выбранную картинку
image = Image.open(random_image)
image.show()