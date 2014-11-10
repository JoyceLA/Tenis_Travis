pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=18 --exclude=*.txt,*.md --max-line-length=200 .
cd UnitTest
python Test_Tenis.py
coverage run --branch Test_Tenis.py
coverage report -m
coverage html --title="Coverage programa Tenis-HTML"
