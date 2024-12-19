<h1 align="center"> Dotenv centralizer </h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/LucasPereiraMiranda/dotenv-centralizer">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/LucasPereiraMiranda/dotenv-centralizer">
  
  <a href="https://github.com/LucasPereiraMiranda/dotenv-centralizer/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/LucasPereiraMiranda/dotenv-centralizer">
  </a>

  <a href="https://github.com/LucasPereiraMiranda/dotenv-centralizer/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/LucasPereiraMiranda/dotenv-centralizer">
  </a>

  <a href="https://github.com/LucasPereiraMiranda/dotenv-centralizer/issues">
    <img alt="GitHub license" src="https://img.shields.io/github/license/LucasPereiraMiranda/dotenv-centralizer">
  </a>
</p>


## 💻 Objectives

A simple tool to centralize and organize multiple .env files in a single directory

## 🚀 Techs

The analysis is being performed with the following technologies:

- [Python3](https://www.python.org/)


## :boom: How we can run the application?

- With python3 & virtualenv already installed, we can run:

```shell
  virtualenv venv

```

- We can activate the virtual environment by running:

```shell
  source venv/bin/activate # Linux or Mac
```

- We can install requirements.txt dependencies:

```shell
  pip install -r requirements.txt
```

- After defining the base directory to analyze .envs recursively in the handle file, we can run:

```shell
  python src/handle.py
```

## 💄 How we can lint app with .pylintrc rules?

- We can run:

```shell
  pylint src/*.py > lint-exceptions.txt
```


### License

[MIT](https://choosealicense.com/licenses/mit/)
