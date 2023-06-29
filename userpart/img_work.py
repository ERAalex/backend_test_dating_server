from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize_and_watermark(image, width, height):
    img = Image.open(image)
    # проверяем размеры для стандартизации всех аватарок
    if img.width > width or img.height > height:
        # сначало добавим метку
        watermark = Image.open('media/images/avatars/love_new.png')
        img.paste(watermark, (0, 0), watermark)

        output_size = (width, height)
        img.thumbnail(output_size)
        # сохраняем имя картинки
        img_filename = Path(image.file.name).name
        # остекаем расширение файла
        img_suffix = Path(image.file.name).name.split(".")[-1]
        img_format = image_types[img_suffix]

        buffer = BytesIO()
        img.save(buffer, format=img_format)

        file_object = File(buffer)
        image.save(img_filename, file_object)
