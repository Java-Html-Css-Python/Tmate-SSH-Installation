import subprocess
import sys

def install_tmate():
    try:
        # Update package lists for upgrades and new packages
        subprocess.check_call(['sudo', 'apt', 'update'])
        
        # Install tmate
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'tmate'])
        
        print("tmate installed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_tmate()
