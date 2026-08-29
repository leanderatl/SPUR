from spur.core.content import Content
from spur.core.state import State
from spur.core.state_repository import StateRepository


def test_state_repository_saves_and_loads_state(tmpdir):
    content = Content(
        name="video_001.mp4",
        path="/programacao/dia_01/video_001.mp4",
        size=500000
    )

    original_state = State([content])

    state_file = tmpdir.join("state.json")

    repository = StateRepository()

    repository.save(
        original_state,
        str(state_file)
    )

    loaded_state = repository.load(
        str(state_file)
    )

    assert len(loaded_state) == 1

    loaded_content = list(loaded_state)[0]

    assert loaded_content.name == "video_001.mp4"
    assert loaded_content.path == "/programacao/dia_01/video_001.mp4"
    assert loaded_content.size == 500000