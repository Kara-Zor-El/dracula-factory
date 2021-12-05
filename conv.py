#!/bin/python
import signal
import argparse
import sys
import os

from pathlib import Path

from ImageGoNord import GoNord

from rich.console import Console
from rich.panel import Panel

# CHANGE pirate TO YOUR OWN USER NAME, DO NOT CHANGE THE DIRECTORY ITSELF
mypath="/home/kara/Pictures/dracula-factory/"

def main():

    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    dr_factory = GoNord()
    dr_factory.reset_palette()
    add_dr_palette(dr_factory)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = fromCommandArgument(console)
    else:
        image_paths = fromTui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, dr_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue

# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture Dracula themed wallpapers."
    )
    command_parser.add_argument(
        "Path", metavar="path", nargs="+", type=str, help="The path(s) to the image(s)."
    )
    args = command_parser.parse_args()

    return args.Path

# Gets the file path from user input
def fromTui(console):

    console.print(
        Panel(
            "🏭 [bold magenta] Dracula Factory [/] 🏭", expand=False, border_style="magenta"
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            "🖼️ [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]

def process_image(image_path, console, dr_factory):
    image = dr_factory.open_image(image_path)
    
    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # TODO: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(
        mypath, "dr_" + os.path.basename(image_path)
    )

    dr_factory.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")

def add_dr_palette(dr_factory):

    drPalette = ["#282936","#3a3c4e","#4d4f68","#626483","#62d6e8","#e9e9f4","#f1f2f8","#f7f7fb","#ea51b2","#b45bcf","#00f769","#ebff87","#a1efe4","#62d6e8","#b45bcf","#00f769"]

    for color in drPalette:
        dr_factory.add_color_to_palette(color)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)

if __name__ == "__main__":
    main()
