#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = os.path.join(os.path.dirname(__file__), "picnic.py")


# --------------------------------------------------
def test_exists():
    """Exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """Usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"{prg} {flag}")
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_one():
    """One item"""

    out = getoutput(f"{prg} chips")
    assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """Two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """More than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"{prg} {arg}")
    expected = "You are bringing potato chips, coleslaw, cupcakes, and French silk pie."
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """Two items sorted output"""

    out = getoutput(f"{prg} -s soda candy")
    assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """More than two items sorted output"""

    arg = "bananas apples dates cherries"
    out = getoutput(f"{prg} {arg} --sorted")
    expected = "You are bringing apples, bananas, cherries, and dates."
    assert out.strip() == expected
