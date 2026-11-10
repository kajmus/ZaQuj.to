
# File for building and running the project
# Run: python build.py

import os
import sys
import platform
import subprocess
import shutil
import shlex
from pathlib import Path

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

FIRST_SETUP = False
BUILD_FRONTEND = False

RUN_DEVELOPMENT = True
RUN_PRODUCTION = False


# --------------------------------------------------
# PATHS
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent

BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"

VENV = BACKEND / "venv"
UVICORN_APP = "app.main:app"


if platform.system() == "Windows":
    VENV_PYTHON = VENV / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV / "bin" / "python"

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def run_command(command, cwd=None):
    """Run command and wait until it finishes."""
    subprocess.run(command, cwd=cwd, check=True)


def setup_venv():
    """Create virtual environment if it doesn't exist."""

    if not VENV_PYTHON.exists():
        print("Creating Python virtual environment...")

        run_command(
            [sys.executable, "-m", "venv", str(VENV)],
            BACKEND
        )

    print("Upgrading pip...")
    run_command(
        [str(VENV_PYTHON), "-m", "pip", "install", "--upgrade", "pip"],
        BACKEND
    )


def install_dependencies():
    """Install backend and frontend dependencies."""

    setup_venv()

    requirements = BACKEND / "requirements.txt"

    if requirements.exists():
        print("Installing backend dependencies...")

        run_command(
            [str(VENV_PYTHON), "-m", "pip", "install", "-r", "requirements.txt"],
            BACKEND
        )
    else:
        print("WARNING: backend/requirements.txt not found.")

    print("Installing frontend dependencies...")

    run_command(["npm.cmd", "install"], FRONTEND)

    print("First setup completed.")


def open_terminal(command, cwd, title):
    """Open a new terminal window and execute command."""

    system = platform.system()

    if system == "Windows":

        powershell_command = f"& {ps_quote(command[0])} " + " ".join(
            ps_quote(arg) for arg in command[1:]
        )

        subprocess.Popen([
            "cmd", "/c", "start", "", "powershell",
            "-NoExit", "-Command",
            f"Set-Location -LiteralPath '{str(cwd)}'; {powershell_command}"
        ])

    elif system == "Linux":

        shell_command = (
            f"cd {shlex.quote(str(cwd))} && "
            f"{shlex.join(command)}; exec bash"
        )

        terminals = [
            (
                "gnome-terminal",
                ["--title", title, "--", "bash", "-c", shell_command]
            ),
            (
                "konsole",
                ["--title", title, "-e", "bash", "-c", shell_command]
            ),
            (
                "xfce4-terminal",
                ["--title", title, "--command", f"bash -c {shlex.quote(shell_command)}"]
            ),
            (
                "xterm",
                ["-T", title, "-e", "bash", "-c", shell_command]
            )
        ]

        for terminal, args in terminals:
            if shutil.which(terminal):
                subprocess.Popen([terminal] + args)
                return

        raise RuntimeError(
            "No supported terminal found. "
            "Install gnome-terminal, konsole, xfce4-terminal or xterm."
        )

    else:
        raise RuntimeError(f"Unsupported OS: {system}")


def ps_quote(value):
    """Escape a string for PowerShell."""
    return "'" + str(value).replace("'", "''") + "'"


def check_venv():
    """Check if virtual environment exists."""

    if not VENV_PYTHON.exists():
        raise RuntimeError(
            "Virtual environment not found. "
            "Set FIRST_SETUP = True and run the script first."
        )


# --------------------------------------------------
# FIRST SETUP
# --------------------------------------------------

if FIRST_SETUP:
    install_dependencies()
    sys.exit(0)


# --------------------------------------------------
# CHECK ENVIRONMENT
# --------------------------------------------------

check_venv()


# --------------------------------------------------
# FRONTEND BUILD
# --------------------------------------------------

if BUILD_FRONTEND:
    print("Building frontend...")

    run_command(
        ["npm", "run", "build"],
        FRONTEND
    )


# --------------------------------------------------
# DEVELOPMENT
# --------------------------------------------------

if RUN_DEVELOPMENT:

    print("Starting development environment...")

    # Backend
    open_terminal(
        [
            str(VENV_PYTHON),
            "-m", "uvicorn",
            UVICORN_APP,
            "--reload"
        ],
        BACKEND,
        "Backend - FastAPI"
    )

    # Frontend
    open_terminal(
        ["npm", "run", "dev"],
        FRONTEND,
        "Frontend - Vite"
    )

    print("Development environment started.")


# --------------------------------------------------
# PRODUCTION
# --------------------------------------------------

if RUN_PRODUCTION:
    print("Production mode is not configured yet.")
