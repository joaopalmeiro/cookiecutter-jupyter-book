# cookiecutter-jupyter-book

A minimal and opinionated [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for bootstrapping [Jupyter Book](http://jupyterbook.org/) projects. It is based on the [`cookiecutter-jupyter-book`](https://github.com/executablebooks/cookiecutter-jupyter-book) template. You can check out a demo [here](https://joaopalmeiro.github.io/cookiecutter-jupyter-book/).

## Quickstart

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
2. `cookiecutter https://github.com/joaopalmeiro/cookiecutter-jupyter-book.git`

## Development

- `pipenv install --dev --python 3.8`
- `pipenv shell`
- `pytest`

## Notes

- Run `touch Pipfile` first in a subdirectory to create a new environment in that subdirectory.
- [actions-gh-pages](https://github.com/peaceiris/actions-gh-pages).
- [actions/cache](https://github.com/actions/cache):
  - [Pipenv](https://github.com/actions/cache/blob/main/examples.md#python---pipenv).
  - [Documentation](https://docs.github.com/en/actions/guides/caching-dependencies-to-speed-up-workflows):
    - `restore-keys` (optional): "An ordered list of alternative keys to use for finding the cache if no cache hit occurred for key."
    - "This example creates a new cache when the packages in `package-lock.json` file change, or when the runner's operating system changes ([both are used to define the `key`]). (...) Using expressions to create a `key` allows you to automatically create a new cache when dependencies have changed."
- Ian Whitestone's [Serverless Python deployments with Github Actions](https://ianwhitestone.work/aws-serverless-deployments-with-github-actions/) blog post:
  - "(...) each `run` keyword represents a new process and shell in the runner environment, so things like environment variables or locally defined variables won't persist between runs."
  - Any of the files in the X directory: `- X/**`.
  - `Pipfile` or `Pipfile.lock`: `- Pipfile*`.
- [pytest-cookies](https://github.com/hackebrot/pytest-cookies):
  - pytest plugin for Cookiecutter templates.
  - `pipenv install --dev pytest pytest-cookies`.
  - `pytest --keep-baked-projects --basetemp=.cookiecutter_projects` (keep the generated projects for testing) or `pytest --keep-baked-projects` + `cd $TMPDIR`.
  - [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) is a reference.
  - It is possible to specify the template directory ([source](https://github.com/hackebrot/pytest-cookies#specify-the-template-directory)).
- `pipenv --rm`.

## References

- Executable Book Project's [`cookiecutter-jupyter-book`](https://github.com/executablebooks/cookiecutter-jupyter-book) Cookiecutter template.
- Connor's [answer](https://stackoverflow.com/a/55435460) on Stack Overflow.
- Support for [SVG favicons](https://caniuse.com/link-icon-svg).
- Chris Coyier's "[Emojis as Favicons](https://css-tricks.com/emojis-as-favicons/)" blog post.
- Lars Wittenberg's [tweet](https://twitter.com/larswittenberg/status/1242465247987810304).
- Chris Coyier's "[Finally, it Will Be Easy to Change the Color of List Bullets](https://css-tricks.com/finally-it-will-be-easy-to-change-the-color-of-list-bullets/)" blog post.
