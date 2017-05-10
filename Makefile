BIN=dpr-ve/bin/


test: 
	$(BIN)/nosetests


cover: 
	$(BIN)/nosetests --with-coverage --cover-erase --cover-package solve_puzzle


lint:
	$(BIN)/pylint *.py
