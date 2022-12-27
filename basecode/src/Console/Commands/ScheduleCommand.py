from datetime import datetime, timedelta
from asyncio import run, get_running_loop, sleep
from scheduler.asyncio import Scheduler
from typer import Typer, echo
from rich.console import Console

class ScheduleCommand:

    async def __call__ (self) -> None:
        """
        :rtype: None
        :raises KeyboardInterrupt:
        """
        schedule = Scheduler (loop = get_running_loop ())

        schedule.cyclic (timedelta (seconds = 5), self.main)

        while True:
            try:
                await sleep (0.1)
            except KeyboardInterrupt:
                break

    async def main (self) -> None:
        """
        :rtype: None
        """
        echo (datetime.now ())

application = Typer ()

name = "schedule"
description = "Run scheduler"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    run (ScheduleCommand () ())
