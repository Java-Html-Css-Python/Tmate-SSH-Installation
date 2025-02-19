#!/usr/bin/env python3
import subprocess
import sys
import platform
import shutil

def install_tmate_apt():
    try:
        print("Using apt-based installation (Debian/Ubuntu)...")
        subprocess.check_call(['sudo', 'apt', 'update'])
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'tmate'])
        print("tmate installed successfully on an apt-based system!")
    except subprocess.CalledProcessError as e:
        print(f"Error during apt installation: {e}")
        sys.exit(1)

def install_tmate_pacman():
    try:
        print("Using pacman-based installation (Arch Linux)...")
        subprocess.check_call(['sudo', 'pacman', '-Syu', '--noconfirm'])
        subprocess.check_call(['sudo', 'pacman', '-S', '--noconfirm', 'tmate'])
        print("tmate installed successfully on a pacman-based system!")
    except subprocess.CalledProcessError as e:
        print(f"Error during pacman installation: {e}")
        sys.exit(1)

def install_tmate_redhat():
    try:
        print("Using Red Hat-based installation (Fedora/CentOS/RHEL)...")
        if shutil.which("dnf"):
            subprocess.check_call(['sudo', 'dnf', 'update', '-y'])
            subprocess.check_call(['sudo', 'dnf', 'install', '-y', 'tmate'])
        elif shutil.which("yum"):
            subprocess.check_call(['sudo', 'yum', 'update', '-y'])
            subprocess.check_call(['sudo', 'yum', 'install', '-y', 'tmate'])
        else:
            print("No recognized Red Hat package manager found (dnf or yum required).")
            sys.exit(1)
        print("tmate installed successfully on a Red Hat-based system!")
    except subprocess.CalledProcessError as e:
        print(f"Error during Red Hat installation: {e}")
        sys.exit(1)

def install_tmate_zypper():
    try:
        print("Using zypper installation (openSUSE/SUSE)...")
        subprocess.check_call(['sudo', 'zypper', 'refresh'])
        subprocess.check_call(['sudo', 'zypper', 'install', '-y', 'tmate'])
        print("tmate installed successfully on a SUSE-based system!")
    except subprocess.CalledProcessError as e:
        print(f"Error during zypper installation: {e}")
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
        print("Starting tmate...")
        subprocess.check_call(['tmate'])
    except subprocess.CalledProcessError as e:
        print(f"Error running tmate: {e}")
        sys.exit(1)

def main():
    current_os = platform.system()
    print(f"Detected OS: {current_os}")

    if current_os == 'Linux':
        # Check for package managers in order
        if shutil.which("apt"):
            install_tmate_apt()
        elif shutil.which("pacman"):
            install_tmate_pacman()
        elif shutil.which("dnf") or shutil.which("yum"):
            install_tmate_redhat()
        elif shutil.which("zypper"):
            install_tmate_zypper()
        else:
            print("Unsupported package manager on Linux. Please install tmate manually.")
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

    # Once installed, automatically run tmate.
    run_tmate()

if __name__ == "__main__":
    main()
