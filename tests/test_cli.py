"""Tests for rust-bridge CLI."""

import pytest
from click.testing import CliRunner
from rust_bridge.cli import main


def test_cli_help():
    """Test that CLI shows help."""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Python-Rust interoperability" in result.output


def test_generate_bindings_command():
    """Test generate-bindings command with basic options."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create a dummy pyproject.toml
        with open("pyproject.toml", "w") as f:
            f.write("""[project]
name = "test-project"
version = "0.1.0"
""")

        result = runner.invoke(main, ["generate-bindings", "pyproject.toml"])
        assert result.exit_code == 0
        assert "Generating pyo3 bindings" in result.output