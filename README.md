brsus
==============================

A tool to download data from datasus.

Project Organization
------------
```
├── .github                       -- scripts for CI/CD
├── brsus -- folder with the lib source code
├── setup.py                      -- setup file for the module to be installable
├── tests                         -- folder with test scripts
├── scripts                       -- folder with bash scripts used for setup the project
├── README.md                     -- description of what the project consists of, how to reproduce it and how to contribute
├── params.yml                    -- file with all parameters used in the project, to facilitate documentation and reproduction
└── pyproject.toml                -- file that specify all code dependencies
```

## How to install
To install run
```
$ poetry install
```
After installing you could access the virtual enviroment with `poetry shell` \
Create a github repository and add the remote origin to do yout project version control.

## How to use
...

## Repo navigation
![Visualization of this repo](./diagram.svg)


## How to contribute
Install all project dependencies (prod and dev)
```
$ poetry install
```

Create your own branch, do your contribution and certifies that the code is complaint with the code standards:
```
$ poetry run fmt-check
$ poetry run isort-check
$ poetry run linter
$ poetry run tests
```
Now, open the pull request and enjoy code review :)