from PySide6.QtWidgets import QApplication
from unittest import TestCase


class QtApplicationTest(TestCase):

    @classmethod
    def setUpClass(cls):
        if not QApplication.instance():
            cls.app = QApplication([])

        else:
            cls.app = QApplication.instance()
