coverage run --source ./StrataAI -m pytest -n 8 --durations=0 --timeout=100 && coverage report -m && coverage html && open htmlcov/index.html
