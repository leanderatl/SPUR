from spur.core.scanner import Scanner


def test_scanner_finds_files(tmpdir):
    file_path = tmpdir.join("video_001.mp4")
    file_path.write("conteudo de teste")

    scanner = Scanner()

    state = scanner.scan(str(tmpdir))

    assert len(state) == 1

    content = list(state)[0]

    assert content.name == "video_001.mp4"
    assert content.size > 0


def test_scanner_ignores_directories(tmpdir):
    file_path = tmpdir.join("video_001.mp4")
    file_path.write("conteudo de teste")

    tmpdir.mkdir("subpasta")

    scanner = Scanner()

    state = scanner.scan(str(tmpdir))

    assert len(state) == 1

    content = list(state)[0]

    assert content.name == "video_001.mp4"