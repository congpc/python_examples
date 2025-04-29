# """test_one_app.py"""
from streamlit.testing.v1 import AppTest

def test_layout():
    at = AppTest.from_file("./one_app/app.py").run(timeout=10)
    assert "Uber pickups in NYC" in at.title[0].value
    