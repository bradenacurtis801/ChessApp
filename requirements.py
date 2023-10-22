import subprocess
import sys

def install_colorama():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])

install_colorama()