#!/usr/bin/env python3
"""tests for hello.py."""

import os
from subprocess import getoutput, getstatusoutput

prg = os.path.join(os.path.dirname(__file__), "hello.py")
run_cmd = f"python3 {prg}"


# --------------------------------------------------
def test_exists():
    """Exists."""
    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3."""
    out = getoutput(run_cmd)
    assert out.strip() == "Hello, World!"


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default."""
    out = getoutput(run_cmd)
    assert out.strip() == "Hello, World!"


# --------------------------------------------------
def test_usage():
    """Usage"""
    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{run_cmd} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_input():
    """Test for input"""
    for val in ["Universe", "Multiverse"]:
        for option in ["-n", "--name"]:
            rv, out = getstatusoutput(f"{run_cmd} {option} {val}")
            assert rv == 0
            assert out.strip() == f"Hello, {val}!"
