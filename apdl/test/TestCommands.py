import unittest
from workhelper.apdl import Commands, Command

class TestCommands(unittest.TestCase):

    def test_append(self):
        cmds = Commands()
        cmds.append(Command("This is a command"))
        self.assertEqual(str(cmds[0]), "This is a command")

    def test_extend(self):
        cmds = Commands()
        cmds.extend([Command("This is a command"), Command("This is another command")])
        self.assertEqual(str(cmds[0]), "This is a command")
        self.assertEqual(str(cmds[1]), "This is another command")
    
    def test_blank(self):
        cmds = Commands()
        cmds.blank()
        self.assertEqual(str(cmds[0]), "")

    def test_comment(self):
        cmds = Commands()
        cmds.comment("This is a comment")
        self.assertEqual(str(cmds[0]), "! This is a comment")

    def test_block(self):
        cmds = Commands()
        cmds.block("This is a block")
        self.assertEqual(repr(cmds), "['', '!*********************************************', '! This is a block', '!*********************************************', '']")

    def test_indent(self):
        cmds = Commands()
        cmds.append(Command("This is a command"))
        cmds.indent = 1
        cmds.append(Command("This is another command"))
        self.assertEqual(str(cmds[0]), "This is a command")
        self.assertEqual(str(cmds[1]), "    This is another command")


if __name__ == "__main__":
    unittest.main()
