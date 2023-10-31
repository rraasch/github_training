# test.py

import json
from main import main

def test_main():
    """this is the test_main function"""
    assert json.loads(main())['message'] == "SUCCESS"
