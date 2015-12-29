# quorce

*quorce* (/kwəɹs/) is a simple, single-user web app to store quotes. This software is **not** stable yet.

## Installation

Clone the repository. Create a virtual environment using `pyvenv venv` (where `venv` is an arbitrary name; you can change it). Activate it (`source venv/bin/activate`). Install required packages using `pip3 install Flask Flask-Misaka`.

## Setting up

Edit `config.py` according to your needs. Create database using `./init_db.py` (**warning**: it will remove your current database).

## Running

### Development

`./quorce.py`. That's all you need.

### Deployment

Set the `SECRET_KEY` and turn off the `DEBUG` flag in `config.py`. Deploy according to the [Flask documentation](http://flask.pocoo.org/docs/0.10/deploying/#deployment).

## FAQ

* What does *quorce* mean?

    *quorce* doesn't mean anything. The name is a portmanteau of the words *quote* and *source*.
