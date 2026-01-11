"""Command-line interface for rust-bridge."""

from pathlib import Path
from typing import Any

import click
from jinja2 import Environment

# Handle tomllib import for different Python versions
_tomllib: Any  # type: ignore[misc]
try:
    import tomllib  # type: ignore[import-not-found]
    _tomllib = tomllib
except ImportError:
    import tomli as tomllib  # type: ignore[import-not-found]
    _tomllib = tomllib


@click.group()
@click.version_option()
def main():
    """Python-Rust interoperability tools and FFI helpers."""
    pass


@main.command()
@click.argument("pyproject_path", type=click.Path(exists=True))
@click.option(
    "--output", "-o", type=click.Path(), help="Output directory for generated bindings"
)
@click.option(
    "--template",
    "-t",
    type=click.Choice(["pyo3", "native", "cbindgen"]),
    default="pyo3",
)
def generate_bindings(pyproject_path, output, template):
    """Generate Rust-Python bindings from pyproject.toml."""
    pyproject_file = Path(pyproject_path)
    output_path = Path(output) if output else pyproject_file.parent / "rust_bindings"

    click.echo(f"🔗 Generating {template} bindings from {pyproject_file}")
    click.echo(f"📁 Output directory: {output_path}")

    # Read pyproject.toml
    with open(pyproject_file, "rb") as f:
        config = _tomllib.load(f)

    project_name = config.get("project", {}).get("name", "unknown")
    click.echo(f"📦 Project: {project_name}")

    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "src").mkdir(parents=True, exist_ok=True)

    if template == "pyo3":
        generate_pyo3_bindings(config, output_path)
    elif template == "native":
        generate_native_bindings(config, output_path)
    elif template == "cbindgen":
        generate_cbindgen_config(config, output_path)

    click.echo("✅ Bindings generated successfully")


def generate_pyo3_bindings(config, output_path):
    """Generate PyO3 bindings."""
    lib_rs_content = """use pyo3::prelude::*;

#[pyfunction]
fn add(a: i32, b: i32) -> PyResult<i32> {
    Ok(a + b)
}

#[pymodule]
fn {{ project_name|replace("-", "_") }}(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
"""

    cargo_toml_content = """[package]
name = "{{ project_name|replace("-", "_") }}"
version = "{{ version }}"
edition = "2021"

[lib]
name = "{{ project_name|replace("-", "_") }}"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.22", features = ["extension-module"] }
"""

    pyo3_setup = """
from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="{{ project_name }}",
    version="{{ version }}",
    rust_extensions=[RustExtension("{{ project_name|replace("-", "_") }}")],
    setup_requires=["setuptools-rust"],
    zip_safe=False,
)
"""

    env = Environment()
    template_lib = env.from_string(lib_rs_content)
    template_cargo = env.from_string(cargo_toml_content)
    template_setup = env.from_string(pyo3_setup)

    project_name = config.get("project", {}).get("name", "unknown")
    version = config.get("project", {}).get("version", "0.1.0")

    # Write lib.rs
    with open(output_path / "src" / "lib.rs", "w") as f:
        f.write(template_lib.render(project_name=project_name, version=version))

    # Write Cargo.toml
    with open(output_path / "Cargo.toml", "w") as f:
        f.write(template_cargo.render(project_name=project_name, version=version))

    # Write setup.py
    with open(output_path / "setup.py", "w") as f:
        f.write(template_setup.render(project_name=project_name, version=version))


def generate_native_bindings(config, output_path):
    """Generate native Python extension bindings."""
    click.echo("Native bindings generation not yet implemented")


def generate_cbindgen_config(config, output_path):
    """Generate cbindgen configuration."""
    cbindgen_toml = """[parse]
parse_deps = true
include = ["your_crate"]

[fn]
rename_args = "SnakeCase"

[struct]
rename_fields = "SnakeCase"

[enum]
rename_variants = "ScreamingSnakeCase"
"""

    with open(output_path / "cbindgen.toml", "w") as f:
        f.write(cbindgen_toml)


@main.command()
@click.argument("rust_project", type=click.Path(exists=True))
@click.option("--python-module", "-m", help="Python module name")
def analyze_rust(rust_project, python_module):
    """Analyze Rust project for Python interop opportunities."""
    rust_path = Path(rust_project)

    click.echo(f"🔍 Analyzing Rust project: {rust_path}")
    click.echo(f"🐍 Python module: {python_module}")

    # TODO: Implement Rust code analysis for Python interop
    click.echo("✅ Analysis completed (placeholder)")


if __name__ == "__main__":
    main()
