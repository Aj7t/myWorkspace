
import pytest
import re

def test_regex():
   regex = r'^[0-9]{6}$'
   try:
      assert(re.match(regex, "842701"))
      print("\033[94m" + "Regex expression is correct\n" + "\033[0m")

   except AssertionError as msg:
      print("\033[91m" + "Regex expression is incorrect\n" + "\033[0m")
