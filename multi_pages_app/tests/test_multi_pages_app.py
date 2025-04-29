# """multi_pages_app.py"""
from streamlit.testing.v1 import AppTest


def test_layout():
    at = AppTest.from_file("./multi_pages_app/Hello.py").run(timeout=20)
    assert "Multi pages" in at.title[0].value
