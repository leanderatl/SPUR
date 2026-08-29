from spur.core.detector import Detector
from spur.core.scanner import Scanner
from spur.core.state import State


def test_first_scan_creates_baseline_without_relocation(tmpdir):
    file_path = tmpdir.join("video_001.mp4")
    file_path.write("conteudo de teste")

    scanner = Scanner()
    detector = Detector()

    current_state = scanner.scan(str(tmpdir))
    previous_state = State([])

    relocations = detector.detect_relocations(
        previous_state=previous_state,
        current_state=current_state
    )

    assert len(current_state) == 1
    assert len(relocations) == 0