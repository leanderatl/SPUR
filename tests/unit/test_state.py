from spur.core.content import Content
from spur.core.state import State


def test_state_starts_empty():
    state = State()

    assert len(state) == 0


def test_state_stores_contents():
    content = Content(
        name="video_001.mp4",
        path="/programacao/dia_01/video_001.mp4",
        size=500000
    )

    state = State()
    state.add(content)

    assert len(state) == 1
    assert list(state)[0] is content