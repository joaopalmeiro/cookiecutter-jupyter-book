# {{ cookiecutter.book_name }}

{{ cookiecutter.book_short_description }}

## Creating a virtual environment

1. `pipenv run --python 3.8`
2. `pipenv shell`

## Building a Jupyter Book

1. `jb clean {{ cookiecutter.book_slug }}/`
2. `jb build {{ cookiecutter.book_slug }}/`
3. `pipenv run serve`
