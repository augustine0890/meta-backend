"""
    Project Zero: A template for other projects
"""
import src.hello_world as app


def test_hello_world(capsys):
    app.main([])
    out, err = capsys.readouterr()
    assert "Hello, World!" in out
