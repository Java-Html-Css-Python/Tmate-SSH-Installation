#!/usr/bin/env python3
import subprocess
import sys
import platform
import shutil
import os

def install_tmate_apt():
    try:
        print("Using apt-based installation...")
        subprocess.check_call(['sudo', 'apt', 'update'])
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'tmate'])
        print("tmate installed successfully on an apt-based system!")
    except subprocess.CalledProcessError as e:
        print(f"Error during apt installation: {e}")
        sys.exit(1)

def install_tmate_brew():
    try:
        print("Using Homebrew installation on macOS...")
        subprocess.check_call(['brew', 'update'])
        subprocess.check_call(['brew', 'install', 'tmate'])
        print("tmate installed successfully on macOS!")
    except subprocess.CalledProcessError as e:
        print(f"Error during Homebrew installation: {e}")
        sys.exit(1)

def install_tmate_choco():
    try:
        print("Using Chocolatey installation on Windows...")
        subprocess.check_call(['choco', 'install', '-y', 'tmate'])
        print("tmate installed successfully on Windows!")
    except subprocess.CalledProcessError as e:
        print(f"Error during Chocolatey installation: {e}")
        sys.exit(1)

def run_tmate():
    try:
        print("Starting tmate interactively...")
        subprocess.check_call(['tmate'])
    except subprocess.CalledProcessError as e:
        print(f"Error running tmate: {e}")
        sys.exit(1)

def main():
    current_os = platform.system()
    print(f"Detected OS: {current_os}")

    if current_os == 'Linux':
        if shutil.which("apt"):
            install_tmate_apt()
        else:
            print("Unsupported Linux package manager. Please install tmate manually.")
            sys.exit(1)
    elif current_os == 'Darwin':  # macOS
        if shutil.which("brew"):
            install_tmate_brew()
        else:
            print("Homebrew is not installed. Please install Homebrew first.")
            sys.exit(1)
    elif current_os == 'Windows':
        if shutil.which("choco"):
            install_tmate_choco()
        else:
            print("Chocolatey is not installed. Please install Chocolatey or install tmate manually.")
            sys.exit(1)
    else:
        print("Unsupported operating system.")
        sys.exit(1)

    # If running in CI, skip the interactive session.
    if os.getenv("CI"):
        print("CI environment detected; skipping interactive tmate session.")
    else:
        run_tmate()

if __name__ == "__main__":
    main()
