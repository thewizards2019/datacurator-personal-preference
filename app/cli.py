import click
from flask.cli import FlaskGroup
from .app import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the app"""


@cli.command("init")
def init():
    """
    Initialize application
    """
    click.echo("Not doing anything...init complete")


cli.add_command(init)
