install:
 pip install -r requirements.txt

test:
 pytest -v

parallel:
 pytest -n 2 -v

report:
 pytest -n 2 -v --html=report.html

clean:
 rm -rf __pycache__
 rm -rf .pytest_cache
 rm -rf report.html