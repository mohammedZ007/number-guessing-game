# Number Guessing Game

A simple Python number guessing game that is containerized using Docker and automatically tested using GitHub Actions.

## Project Overview

The application generates a random number between 1 and 10.

The player gets 3 chances to guess the number.

- Correct guess → Player wins
- Difference of 2 or less → "Near"
- Difference greater than 2 → "Far"
- Number outside 1–10 → Invalid input
- Non-numeric input → Invalid input

## Project Structure

```text
number-guessing-game/
├── app/
│   └── app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
└── README.md
