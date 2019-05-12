HIDE := @
activate: create-venv
	$(HIDE)( \
       source env/bin/activate; \
       pip install -r requirements.txt; \
       python3 source.py; \
    )

create-venv: 
	$(HIDE)python3 -m venv env