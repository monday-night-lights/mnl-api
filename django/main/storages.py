from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = settings.STATIC_DIRNAME
    default_acl = 'public-read'


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIA_DIRNAME
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'media-private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False