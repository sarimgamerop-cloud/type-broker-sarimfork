# Contributing to Type-Broker

First off, thank you for considering contributing to Type-Broker! It's people like you that make Type-Broker such a great tool.

> ⚠️ **Disclaimer:** As stated in the README, this project is **STRICTLY FOR EDUCATIONAL AND LEARNING PURPOSES.** We do not accept contributions that aim to enhance the project's capability to natively cheat or bypass competitive platforms' anti-cheat mechanisms. Contributions should focus on improving OCR accuracy, UI/UX, multi-platform support, and code quality.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check if there's already an open issue for it. If not, feel free to open a new issue.

## Setting up your environment

Type-Broker relies on specific system dependencies. Depending on your OS, follow the setup instructions in the `README.md`.

### For Ubuntu/Debian (Xorg)
1. Install system dependencies:
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr wmctrl gnome-screenshot python3-tk
   ```
2. Setup the Python environment using `uv`:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

### For NixOS Users
A `flake.nix` is provided for a reproducible development environment.
1. Enter the development shell:
   ```bash
   nix develop
   ```
   *The shell hook will automatically create a virtual environment and sync Python dependencies using `uv`.*

### For Windows Users
Make sure you have installed the native `tesseract.exe` as mentioned in the README.

## How to Contribute

### Reporting Bugs

Bugs are tracked as GitHub issues. When creating an issue, please explain the problem and include additional details to help maintainers reproduce the problem:
* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include links to files or copy/pasteable snippets, which you use in those examples.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include details about your environment** (OS, Xorg/Wayland/Windows, Python version).

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement issue, please include:
* **A clear and descriptive title**.
* **A step-by-step description of the suggested enhancement**.
* **Specific examples to demonstrate the steps** (e.g., mockups, UI designs).
* **Explain why this enhancement would be useful** to most Type-Broker users.

### Pull Requests

1. **Fork the repository** and clone it locally.
2. **Create a new branch** specifically for your feature or bugfix (e.g., `git checkout -b feature/amazing-feature`).
3. **Make your changes**. 
4. **Test your changes** thoroughly. Ensure it doesn't break existing functionality on supported platforms (Windows, Ubuntu (Xorg), NixOS).
5. **Commit your changes** with descriptive commit messages.
6. **Push to the branch** (`git push origin feature/amazing-feature`).
7. **Open a Pull Request** against the main repository. Detailed description of the changes is highly appreciated.

## Styleguides

### Git Commit Messages
* Use the present tense ("Add feature" not "Added feature").
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
* Limit the first line to 72 characters or less.
* Reference issues and pull requests liberally after the first line.

### Python Styleguide
* We recommend following PEP 8.
* Keep the Code easily readable, documented and clean.

Thank you for contributing!
