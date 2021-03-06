from unittest import TestCase
from unittest.mock import Mock

from model.system import *


class SystemTest(TestCase):
    def test_output_system(self):
        output = Mock()
        s = OutputSystem(1, output)
        s.set_level(0.5)
        output.set_level.assert_called_once_with(1, 0.5)

    def test_compound_system(self):
        outputs = [Mock(), Mock(), Mock()]
        cs = CompoundSystem([
            OutputSystem(1, outputs[0]),
            CompoundSystem([
                OutputSystem(1, outputs[1]),
                OutputSystem(1, outputs[2])
            ])
        ])
        cs.set_level(0.25)
        for output in outputs:
            output.set_level.assert_called_once_with(1, 0.25)

# TODO add test case for output

# TODO add test case for settings
