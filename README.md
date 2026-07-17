# py-rust-bridge

<!-- FLEET-BADGES:BEGIN -->
[![CI](https://github.com/tzervas/py-rust-bridge/actions/workflows/fleet-ci.yml/badge.svg?branch=main)](https://github.com/tzervas/py-rust-bridge/actions/workflows/fleet-ci.yml?query=branch%3Amain)
[![Security](https://github.com/tzervas/py-rust-bridge/actions/workflows/fleet-security.yml/badge.svg?branch=main)](https://github.com/tzervas/py-rust-bridge/actions/workflows/fleet-security.yml?query=branch%3Amain)
<!-- FLEET-BADGES:END -->

Python-Rust interoperability tools and FFI helpers for seamless language integration.

## Installation

```bash
pip install py-rust-bridge
```

## Usage

Generate PyO3 bindings from pyproject.toml:

```bash
rust-bridge generate-bindings pyproject.toml --template pyo3
```

Analyze Rust project for Python interop:

```bash
rust-bridge analyze-rust ./rust-project --python-module mymodule
```

## Features

- **PyO3 Bindings Generation**: Automatic generation of PyO3 Rust extensions from Python project metadata
- **Template Support**: Multiple binding templates (PyO3, native extensions, cbindgen)
- **Rust Code Analysis**: Identify functions and types suitable for Python exposure
- **FFI Helpers**: Utilities for foreign function interface development

## Dependencies

- Compatible with PyO3 (Apache-2.0/MIT dual license)
- Uses setuptools-rust for building Rust extensions
- Supports Python 3.9+ with conditional tomllib/tomli usage

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Format code
uv run black src/
uv run isort src/
```

## License

MIT License - see [LICENSE](LICENSE) for details.