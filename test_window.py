import unittest

from window import Window


class WindowTestCase(unittest.TestCase):

    def test_default_values(self):
        window = Window.new_builder().build();
        self.assertEqual(window.get_x(), 0)
        self.assertEqual(window.get_y(), 0)
        self.assertEqual(window.get_width(), 100)
        self.assertEqual(window.get_height(), 100)
        self.assertEqual(window.get_title(), "")

    def test_non_default_values(self):
        window = Window.new_builder().x(20).y(20).width(200).height(200).title("title").build();
        self.assertEqual(window.get_x(), 20)
        self.assertEqual(window.get_y(), 20)
        self.assertEqual(window.get_width(), 200)
        self.assertEqual(window.get_height(), 200)
        self.assertEqual(window.get_title(), "title")


if __name__ == '__main__':
    unittest.main()