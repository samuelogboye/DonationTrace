import cloudinary.uploader

def upload_image_and_get_url(image_file, folder):
    # Upload the image file to Cloudinary
    try:
        response = cloudinary.uploader.upload(image_file, folder=folder)

        return response.get('url')
    except Exception as e:
        raise Exception(f"Failed to upload image: {str(e)}")

def upload_pdf_and_get_url(pdf_file, folder):
    # Upload the PDF file to Cloudinary
    upload_response = cloudinary.uploader.upload(
        pdf_file,
        resource_type='raw',
        folder=folder
    )
    return upload_response.get('url')
