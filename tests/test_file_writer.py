from src.find_nearby_earthquakes.file_writer import FileWriter


def test_write_text(tmp_path):
    CONTENT = 'Hello There!'

    d = tmp_path / "sub"
    d.mkdir()
    path = d / "hello.txt"

    fw = FileWriter()
    fw.write_text(CONTENT, path)
    assert len(list(tmp_path.iterdir())) == 1
