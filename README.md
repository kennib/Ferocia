# Ferocia term deposit calculator

## Cloud dev environment
You can go to the online dev environment at [codesandbox.io](https://codesandbox.io/p/github/kennib/Ferocia)

## Setup and run locally

To set up, assuming you have python3.10 or greater installed:

```bash
pip install poetry
poetry install
```

To run:

```bash
poetry run python main.py
```

And open [localhost:8000](http://localhost:8000) in your browser.

## Run tests
There are only trivial doc tests.
Run the following command to run them.

```
poetry run python calculations.py
```

## TODO
If I were to continue this theoretical project, here are the things I would focus on:
* More testing/error handling
    * Use a more suitable testing framework (e.g., pytest instead of doctest)
    * End to end tests (using [Playwright](https://playwright.dev/python/) or similar)
    * Better type boundary enforcement (e.g., see what happens when you submit an invalid payment schedule value)
    * test corner cases (e.g., rounding of values)
* Better UI
    * CSS
    * Dynamic update of results (using HTMX)
    * Formatting of input fields (e.g., commas in deposit value)
    * Help text for confusing fields
    * A better term input which allows for months in addition to years