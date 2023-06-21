# psycopg2

- https://www.psycopg.org/docs/
- https://github.com/psycopg/psycopg2
- https://pypi.org/project/psycopg2/

__venv:__

    python3 -m venv .venv && . .venv/bin/activate

__Running:__

    pytest

__Coverage:__

    coverage run -m pytest
    coverage html

    pytest --cov . --cov-report html

__Running:__

    python -m unittest discover -v
    python -m unittest discover -p 'test_*.py'

__Coverage:__

    coverage run -m unittest discover
    coverage report -m
    coverage html
