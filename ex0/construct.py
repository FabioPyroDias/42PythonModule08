import sys
import os
import site


if __name__ == "__main__":
    # sys.prefix - A string giving the site-specific directory prefix where
    #              the platform independent Python files are installed
    # sys.base_prefix - Equivalent to prefix, but referring to the
    #                   base Python installation.
    #                   When running under virtual environment, prefix gets
    #                   overwritten to the virtual environment prefix.
    #                   base_prefix, conversely, does not change,
    #                   and always points to the base Python installation
    if sys.prefix == sys.base_prefix:
        # If prefix is the same as base_prefix, were not in a
        # Virtual Environment
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")
        print()
        print("Then run this program again.")
    else:
        # sys.prefix, while inside a VE, is overwritten to the directory where
        # the platform independent Python files are installed in that VE.
        # With such information, we can know if we are inside a VE or not.
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        # sys.executable - A string giving the absolute path of the executable
        #                  binary for the Python interpreter,
        #                  on systems where this makes sense.
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        # site.getsitepackages() - returns a list of directories where Python
        #                          usually installs non-specific user packages.
        #                          In other words, these are global paths
        #                          where Python looks for packages
        #                          installed by pip
        # Getting the first result on that list, [0],
        # gets the package installation path
        print("Package installation path:")
        print(site.getsitepackages()[0])
