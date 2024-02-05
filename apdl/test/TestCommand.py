import unittest
from workhelper.apdl.Command import Command


class TestCommand(unittest.TestCase):
    def test_init(self):
        cmd = Command("test")
        self.assertEqual(cmd.cmd, "test")
        self.assertEqual(cmd.indent, 0)
        self.assertEqual(cmd.is_comment, False)

    def test_comment(self):
        cmd = Command("test", is_comment=True)
        self.assertEqual(str(cmd), "! test")

    def test_add(self):
        cmd1 = Command("test1")
        cmd2 = Command("test2")
        cmd3 = cmd1 + cmd2
        self.assertEqual(cmd3.cmd, "test1$test2")
        self.assertEqual(cmd3.indent, 0)
        self.assertEqual(cmd3.is_comment, False)
        cmd1 += cmd2
        self.assertEqual(cmd1.cmd, "test1$test2")
        self.assertEqual(cmd1.indent, 0)
        self.assertEqual(cmd1.is_comment, False)
        cmd4 = Command("test4", is_comment=True)
        with self.assertRaises(Exception):
            cmd1 += cmd4
        with self.assertRaises(Exception):
            cmd1 + cmd4

    def test_indent(self):
        cmd = Command("test")
        cmd.indent = 1
        self.assertEqual(str(cmd), "    test")


if __name__ == "__main__":
    unittest.main()
