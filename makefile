venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


run: venv/bin/activate
	./venv/bin/python3 algorithms/search_algorithms.py

test: venv/bin/activate
	./venv/bin/python3 tests/test_search_algorithms.py
	./venv/bin/python3 tests/test_practice_problems.py

clean:
	rm -rf algorithms/__pycache__
	rm -rf venv 
