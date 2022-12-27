from .Version import Version
from .Console.Commands.VersionCommand import application as VersionCommand, name as VersionCommandName, description as VersionCommandDescription
from .Console.Commands.CommunicationCommand import application as CommunicationCommand, name as CommunicationCommandName, description as CommunicationCommandDescription
from .Console.Commands.ScheduleCommand import application as ScheduleCommand, name as ScheduleCommandName, description as ScheduleCommandDescription
from dotenv import load_dotenv
from os import environ
from typer import Typer

load_dotenv ()

application = Typer (help = environ.get ("PYTHON_NAME", "Command Line Tool"))

application.add_typer (VersionCommand, name = VersionCommandName, help = VersionCommandDescription)
application.add_typer (CommunicationCommand, name = CommunicationCommandName, help = CommunicationCommandDescription)
application.add_typer (ScheduleCommand, name = ScheduleCommandName, help = ScheduleCommandDescription)

if __name__ == "__main__":

    application ()
