#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = os.path.join(os.path.dirname(__file__), 'jump.py')


# --------------------------------------------------
def test_exists():
    """Exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """Usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """Test"""

    rv, out = getstatusoutput(f'{prg} 123-456-7890')
    assert rv == 0
    assert out == '987-604-3215'


# --------------------------------------------------
def test_02():
    """Test"""

    rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.rstrip() == 'That number to call is 512-340-6789.'
