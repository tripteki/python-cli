from sys import argv
from os import system

def main ():
    """
    :rtype: None
    """
    command = " ".join ([argv[1]]+argv[1:]) if len (argv) > 1 else "--help"
    system (f"/usr/bin/env python3 -m basecode.src.___main___ {command}")

if __name__ == "__main__":

    main ()
