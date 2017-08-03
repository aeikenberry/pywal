"""Test __main__ functions."""
import unittest
from unittest.mock import MagicMock

from pywal import __main__
from pywal import colors
from pywal import export
from pywal import image
from pywal import reload
from pywal import sequences
from pywal.settings import CACHE_DIR


class TestMain(unittest.TestCase):
    """Test the gen_colors functions."""

    def test_clean(self):
        """> Test arg parsing (-c)"""
        args = __main__.get_args(["-c"])
        __main__.process_args(args)
        self.assertFalse((CACHE_DIR / "schemes").is_dir())

    def test_args_e(self):
        """> Test arg parsing (-e)"""
        reload.env = MagicMock()
        image.get = MagicMock()
        colors.get = MagicMock()
        sequences.send = MagicMock()
        export.every = MagicMock()

        # Test is not called with -e
        args = __main__.get_args(["-e", "-i /path.jpg"])
        __main__.process_args(args)

        self.assertTrue(image.get.called)
        self.assertTrue(colors.get.called)
        self.assertTrue(sequences.send.called)
        self.assertFalse(reload.env.called)

        # Is called without -e
        args = __main__.get_args(["-i /path.jpg"])
        __main__.process_args(args)

        self.assertTrue(reload.env.called)



if __name__ == "__main__":
    unittest.main()
