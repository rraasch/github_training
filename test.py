# test.py

import pytest
import json
from main import main


def test_main():
    assert json.loads(main())['message'] == "SUCCESS"