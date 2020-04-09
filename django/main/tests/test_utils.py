from django.core.exceptions import ValidationError
from django.test import TestCase

from main.utils import extension, slugified_file_location, validate_file_ext


class NamedObject(object):
    def __init__(self, name):
        self.name = name


class UnnamedObject(object):
    def __str__(self):
        return 'unnamed object'


class MainUtilsTestCase(TestCase):

    def test_extension(self):
        for input, expected_output in [
            ('picture.png', 'png'),
            ('picture.of.me.png', 'png'),
            ('picture', None),
            (None, None),
            (True, None),
            (1, None),
            (object, None),
        ]:
            self.assertEqual(extension(input), expected_output)

    def test_slugified_file_location(self):
        for instance, filename, expected_output in [
            (NamedObject('mnl video'), 'cLoaG.mov', 'av/mnl-video.mov'),
            (NamedObject('mnl audio'), 'NCu2H.mp3', 'av/mnl-audio.mp3'),
            (NamedObject('mnl image'), 'wo3BD.png', 'img/mnl-image.png'),
            (NamedObject('mnl doc'), 'Bhp1j.pdf', 'doc/mnl-doc.pdf'),
            (UnnamedObject(), 'FAF1I.docx', 'doc/unnamed-object.docx'),
        ]:
            self.assertEqual(
                slugified_file_location(instance, filename), expected_output)

    def test_validate_file_ext(self):
        for field, filename, allowed_exts in [
            ('logo', 'whalers.bmp', ['png', 'jpg']),
            ('goal_horn', 'whalers.ogg', ['mp3',]),
            ('stats', 'fall-2020.csv', ['xlsx',]),
        ]:
            with self.assertRaises(ValidationError):
                validate_file_ext(field, filename, allowed_exts)
