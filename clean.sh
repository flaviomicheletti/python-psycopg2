echo "Remove __pycache__ files"
sudo find . -type d -name __pycache__ -exec rm -r {} \+
sudo find . -type d -name .pytest_cache -exec rm -r {} \+
sudo find . -type d -name .coverage -exec rm -r {} \+
sudo find . -type d -name htmlcov -exec rm -r {} \+
# sudo find . -type d -name .venv -exec rm -r {} \+        