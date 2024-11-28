---
description: "How to install pdgen on your system using pip. Learn about prerequisites, installation instructions, verification, troubleshooting, and next steps."
---

# Pdgen - UML Diagram Generation - Installation

Installing `pdgen` is straightforward. This page will guide you through the process of getting `pdgen` set up on your
system so you can start generating UML class diagrams from your Python code.

## Prerequisites

Before you install `pdgen`, ensure you meet the following requirements:

- Python 3.12 or newer
- pip (Python package installer)

## Installing pdgen

You can install `pdgen` using pip, Python's package manager. Open your terminal and run the following command:

```bash
pip install pdgen
```

This command will download and install the latest version of `pdgen` and all required dependencies.

## Troubleshooting

If you encounter any issues during the installation, here are a few common problems and solutions:

- **Permission Errors**: If you receive a permission error, try installing `pdgen` with administrative privileges or use
  a virtual environment.

  ```bash
  sudo pip install pdgen
  ```

- **Dependency Conflicts**: If there are conflicts with existing packages, consider installing `pdgen` in a virtual
  environment using `venv` or `conda`.

  ```bash
  python -m venv pdgen-env
  source pdgen-env/bin/activate
  pip install pdgen
  ```

## Next Steps

With `pdgen` installed, you're ready to start generating UML diagrams from your Python code. Head over to
the [Usage](/guide/usage) page to learn how to use `pdgen` effectively.