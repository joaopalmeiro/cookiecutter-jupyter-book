# {{ cookiecutter.book_name }}

{{ cookiecutter.book_short_description }}

## Creating a virtual environment

1. `pipenv run --python 3.8`
2. `pipenv shell`

## Building a Jupyter Book

1. `jb clean {{ cookiecutter.book_slug }}/`
2. `jb build {{ cookiecutter.book_slug }}/`
3. `pipenv run serve`

## Checking the configuration passed to Sphinx

- `jb config sphinx {{ cookiecutter.book_slug }}/`

### Default `html_theme_options`

The default `html_theme_options` that are passed to Sphinx when this key is not present in the `_config.yml` file are as follows:

```python
html_theme_options = {
    "search_bar_text": "Search this book...",
    "launch_buttons": {
        "notebook_interface": "classic",
        "binderhub_url": "https://mybinder.org",
        "jupyterhub_url": "",
        "thebe": False,
        "colab_url": "",
    },
    "path_to_docs": "",
    "repository_url": "https://github.com/executablebooks/jupyter-book",
    "repository_branch": "master",
    "google_analytics_id": "",
    "extra_navbar": 'Powered by <a href="https://jupyterbook.org">Jupyter Book</a>',
    "extra_footer": "",
    "home_page_in_toc": True,
    "use_repository_button": False,
    "use_edit_page_button": False,
    "use_issues_button": False,
}
```
