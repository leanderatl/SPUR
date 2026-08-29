from spur.core.content import Content
from spur.core.state import State
from spur.core.detector import Detector


def test_detects_content_relocation():
    previous_content = Content(
        name="video_001.mp4",
        path="/programacao/dia_01/video_001.mp4",
        size=500000
    )

    current_content = Content(
        name="video_001.mp4",
        path="/programacao/dia_02/video_001.mp4",
        size=500000
    )

    previous_state = State([previous_content])
    current_state = State([current_content])

    detector = Detector()

    relocations = detector.detect_relocations(
        previous_state,
        current_state
    )

    assert len(relocations) == 1

    event = relocations[0]

    assert event.content_name == "video_001.mp4"
    assert event.previous_path == "/programacao/dia_01/video_001.mp4"
    assert event.current_path == "/programacao/dia_02/video_001.mp4"


def test_does_not_detect_relocation_when_path_is_unchanged():
    previous_content = Content(
        name="video_001.mp4",
        path="/programacao/dia_01/video_001.mp4",
        size=500000
    )

    current_content = Content(
        name="video_001.mp4",
        path="/programacao/dia_01/video_001.mp4",
        size=500000
    )

    previous_state = State([previous_content])
    current_state = State([current_content])

    detector = Detector()

    relocations = detector.detect_relocations(
        previous_state,
        current_state
    )

    assert len(relocations) == 0


def test_does_not_detect_new_content_as_relocation():
    previous_state = State([])

    new_content = Content(
        name="video_002.mp4",
        path="/programacao/dia_02/video_002.mp4",
        size=750000
    )

    current_state = State([new_content])

    detector = Detector()

    relocations = detector.detect_relocations(
        previous_state,
        current_state
    )

    assert len(relocations) == 0