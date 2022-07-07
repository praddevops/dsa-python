venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


run: venv/bin/activate
	./venv/bin/python3 algorithms/algorithm_1.py

test: venv/bin/activate
	./venv/bin/python3 tests/test_algorithms_1.py

clean:
	rm -rf __pycache__
	rm -rf venvb 
