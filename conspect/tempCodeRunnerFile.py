def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Missing required keys in the image data dictionary")
    return f"Image {img['image_title']} has id {img['image_id']}"

print(image_info({'image_title': 'My Cat', 'image_id': 123}))