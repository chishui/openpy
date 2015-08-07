import sys
import unittest
import os
sys.path.insert(0, '../')

cases = [
{
	"operation" : "add",
	"path"		: "./test/hello world",
	"result"	: True,
},
{
	"operation" : "add",
	"path"		: "./test/hello",
	"result"	: False,
},
{
	"operation" : "add",
	"path"		: "./test/hello world/test wired file.txt",
	"result"	: True,
},
# {
# 	"operation" : "remove",
# 	"path"		: "./test/hello world",
# 	"result"	: True,
# },
# {
# 	"operation" : "remove",
# 	"path"		: "./test/hello",
# 	"result"	: False,
# },
# {
# 	"operation" : "remove",
# 	"path"		: "./test/hello world/test wired file.txt",
# 	"result"	: True,
# },
]

from config import Config
class TestConfig(unittest.TestCase):
    config = Config()
    def test(self):
    	for case in cases:
    		if case["operation"] == "add":
    			self.assertEqual(self.config.add_path(case["path"]), case["result"])
    		elif case["operation"] == "remove":
    			self.assertEqual(self.config.remove_path(case["path"]), case["result"])

if __name__ == '__main__':
    unittest.main()