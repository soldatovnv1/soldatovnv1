from pages.about import about_page
from pages.about import images
from PIL import Image
import os

def test_site(browser):
    aboutt_page = about_page(browser)
    aboutt_page.open()
    aboutt_page.about()

def test_images2(browser):
    from pages.about import width_max, width_min, height_max, height_min
    aboutt_page = about_page(browser)
    aboutt_page.open()
    counter = 1
    for img in images:
        IMG = aboutt_page.download_image(img)
        with Image.open(IMG) as IMG:
            image_width, image_height = IMG.size
            width = IMG.size[0]
            height = IMG.size[1]
            width_min = min(width_min, width)
            width_max = max(width_max, width)
            height_min = min(height_min, height)
            height_max = max(height_max, height)
            assert width_min == width_max
            assert height_min == height_max

        os.remove(f'work{counter}.jpg')
        counter += 1