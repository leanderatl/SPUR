from spur.core.detector import Detector
from spur.core.scanner import Scanner


def test_relocation_flow(tmpdir):
    previous_dir = tmpdir.mkdir("estado_anterior")
    current_dir = tmpdir.mkdir("estado_atual")

    previous_file = previous_dir.join("video_001.mp4")
    previous_file.write("conteudo de teste")

    current_file = current_dir.join("video_001.mp4")
    current_file.write("conteudo de teste")

    scanner = Scanner()

    previous_state = scanner.scan(str(previous_dir))
    current_state = scanner.scan(str(current_dir))

    detector = Detector()

    events = detector.detect_relocations(
        previous_state,
        current_state
    )

    assert len(events) == 1

    event = events[0]

    assert event.content_name == "video_001.mp4"
    assert event.previous_path != event.current_path