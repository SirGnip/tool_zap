# tool_zap
Collection of command line string processing tools that can be used locally or remotely


# Components

- Command line tools that do string processing on stdin. Useful as part of unix-style command line pipelines.
- Webserver and bootstrap commands that allow one-file command line tools to be used on remote computers via `curl`. 
- RPC server to support command line tools

These components could potentially be split out into independent projects at a later time.

  
# How to run tools against the code

    # create and activate virtual environment
    python -m venv venv  # or `py -3.7 -m venv venv`
    source venv/Scripts/activate
    
    # install to current environment (with current dir at top of repo) 
    pip install .     # "static" install
    pip install -e .  # "editable" install (setup.py handles source being under `src/`)

    # run app from instal
    python -m gnp
    
    # run app directly from local repo (with current dir at top of repo)
    cd src/
    python -m gnp
    
    # run tests: path-based 
    python -m pytest tests/
    python -m pytest tests/test_common.py
    python -m pytest tests/sub
    # run tests: package syntax
    python -m pytest --pyargs tests.sub

    # run tests with coverage metrics
    python -m pytest --cov tests/
    python -m pytest --cov tests/sub
    python -m pytest --cov tests.sub

    # run linting
    pylint src/  # recurses into directory
    pylint src/ tests/
    pylint gnp.common  # can use package names to lint what is installed

    cd src
    mypy -p gnp
    mypy -p gnp.common
    mypy -m gnp.common.util


# Running app from PyCharm

## Use Default Python Interpreter from PyCharm
- For `src/`, do "Mark Directory" and set as "Sources Root" (folder turns light blue) 
- Right click on `src/gnp/__main__.py` and choose "Run \_\_main\_\_"
    - This relies on the Run Configuration having "Add source roots to PYTHONPATH" set to true (the default)

## Use local venv
- Create venv
- Install package into the venv (ex: `pip install -e .`)
- Set venv as the project's Python interpreter in PyCharm
- Right click on `src/gnp/__misc__.py` and choose "Run \_\_main\_\_"
    - Note: This does NOT rely on a Sources Root folder being set or PYTHONPATH in the Run Configuration.
