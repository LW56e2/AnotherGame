"""
Idea: This will be a game coded using pygame. I want this project to be long
and expandable, and I will add graphics to it by importing small drawings
from GIMP. I also want to use a non-default font and more sophisticated
layout, colors, etc.

Game concept: A 2D game from a birds eye view of a character in a zombie
apocalypse, featuring different weapons, monsters, and levels.

OOP Structure: I will have a main game class "Game" that will contain all
the settings and methods for the game. I will then have an "Entity" class.
All Entity instances will have a few common attributes - entity.location,
entity.velocity, entity.acceleration, and methods - movement_update()
Euler's integration method for acceleration and velocity updates on velocity
and position, render() rendering the object at its location. We will use a
custom class 2D vector class for the location, velocity, and acceleration.

JustAnotherSurvivalGame/
│
├── assets/                   # For storing game assets like images, fonts, and sounds
│   ├── fonts/                # Custom fonts
│   ├── images/               # Graphics for characters, environments, etc.
│   └── sounds/               # Audio files
│
├── src/                      # Source files for your game
│   ├── main.py               # Entry point of the game, initializes the game environment
│   ├── settings.py           # Configuration file for game settings
│   ├── entities/             # Folder for all entity classes
│   │   ├── __init__.py       # Makes entities a Python package
│   │   ├── entity.py         # Base class for all entities
│   │   ├── player.py         # Player subclass
│   │   ├── enemy.py          # Enemy subclass
│   │   └── bullet.py         # Bullet subclass
│   └── utilities/            # Utility functions and classes
│       ├── __init__.py       # Makes utilities a Python package
│       ├── collision.py      # Collision detection functions
│       ├── graphics.py       # Graphics-related utility functions
│       └── sound.py          # Sound management functions
│
└── README.md                 # Project overview and instructions


Currently working on:
Main game loop, player movement, and rendering.

Future to-do list:


"""
import pygame


