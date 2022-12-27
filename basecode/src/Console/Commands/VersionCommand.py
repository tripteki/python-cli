from ...Version import Version
from typer import Typer, echo
from rich.console import Console

application = Typer ()

name = "version"
description = "The version of application"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    version = Version () ()

    if version != None:
        echo (version)
    else:
        Console (stderr = True).print (1)
