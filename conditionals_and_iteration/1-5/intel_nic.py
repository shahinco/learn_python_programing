# """
# install_ixgbe_basic.py Script for Download and Install Intel NIC Driver for ATOM servers.
# Basic Python script to download, extract, compile, and install the ixgbe driver on Ubuntu 16.04 LTS.
# """

import os
import subprocess
import urllib
import tarfile

# Constants
DRIVER_URL = "https://downloadmirror.intel.com/856156/ixgbe-6.1.4.tar.gz"
DEST_DIR = "/var/tmp"
ARCHIVE_NAME = "ixgbe-6.1.4.tar.gz"
ARCHIVE_PATH = os.path.join(DEST_DIR, ARCHIVE_NAME)
EXTRACT_DIR = os.path.join(DEST_DIR, "ixgbe-6.1.4")

def run_command(cmd):
    print("Executing: {}".format(cmd))
    ret = subprocess.call(cmd, shell=True)
    if ret == 0:
        print("Done!")
    else:
        print("Failed!")
    print("")

def main():
    print("<===> Step 1: Downloading Intel Driver from repo <===>")
    print("Downloading from: {}".format(DRIVER_URL))
    urllib.urlretrieve(DRIVER_URL, ARCHIVE_PATH)
    print("Downloading to: {}".format(ARCHIVE_PATH))
    print("")

    print("<===> Step 2: Extracting Driver <===>")
    tar = tarfile.open(ARCHIVE_PATH,"r:gz")
    tar.extractall(path=DEST_DIR)
    tar.close()
    print("Extracted to: {}".format(EXTRACT_DIR))
    print("")

    print("<===> Step 3: Compiling and Installing Driver <===>")
    os.chdir(os.path.join(EXTRACT_DIR, "src"))
    run_command("make clean")
    run_command("make install")

    print("<===> Step 4: Loading Intel ixgbe module <===>")
    run_command("modprobe ixgbe")

    print("<<===>> All Steps Completed! <<===>>")

if __name__ == "__main__":
    main()