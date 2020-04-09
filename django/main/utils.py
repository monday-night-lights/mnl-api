from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify


IMG_EXTS = ['apng', 'bmp', 'gif', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png', 'svg', 'webp',]
AV_EXTS = ['3gp', 'aac', 'flac', 'mpg', 'mpeg', 'mp3', 'mp4', 'm4a', 'm4v', 'm4p', 'oga', 'ogv', 'ogg', 'mov', 'wav', 'webm',]


def extension(filename):
    filename = str(filename)
    return filename.split('.')[-1].lower() if '.' in filename else None


def slugified_file_location(instance, filename):
    name = slugify(instance.name if hasattr(instance, 'name') else instance)
    ext = extension(filename)
    filetype = 'av' if ext in AV_EXTS else 'img' if ext in IMG_EXTS else 'doc'
    return f'{filetype}/{name}.{ext}'


def validate_file_ext(field, filename, allowed_exts):
    ext = extension(filename)
    if ext not in allowed_exts:
        allowed_exts = ', '.join(allowed_exts)
        validation_dict = {}
        validation_dict[field] = [f'Cannot use {ext} file type. Must be {allowed_exts}.']
        raise ValidationError(validation_dict)
