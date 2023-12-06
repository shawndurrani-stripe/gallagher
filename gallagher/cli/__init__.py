"""


"""
import typer

from gallagher import __version__

from .alarms import app as alarms_app
from .cardholders import app as cardholders_app

# Main Typer app use to create the CLI
app = typer.Typer()
app.add_typer(alarms_app, name="alarms")
app.add_typer(cardholders_app, name="ch")


@app.command()
def echo(name: str):
    """

    """
    typer.echo("Hello World")


if __name__ == "__main__":
    """ In case you are invoking this via Python directly

    This is probably never actually used but it is here for completeness.
    You'd execute this by running `python -m gallagher.cli`
    """
    app()
