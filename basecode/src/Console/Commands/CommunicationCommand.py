from os import set_blocking, fdopen
from typer import Typer, echo
from rich.console import Console

application = Typer ()

name = "pipe"
description = "Pipe continuous communication"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    :raises KeyboardInterrupt:
    """
    set_blocking (0, False)

    fd0 = fdopen (0, "rb", 0)
    fd1 = fdopen (1, "wb", 0)

    response = None

    while True:
        try:
            request = fd0.read ()
        except KeyboardInterrupt:
            fd1.close ()
            fd0.close ()
            break

        if request is None: continue
        if not request: break

        if request.decode ("utf-8") == "true\n":
            response = 0
            echo (response)
        if request.decode ("utf-8") == "false\n":
            response = 1
            Console (stderr = True).print (response)
