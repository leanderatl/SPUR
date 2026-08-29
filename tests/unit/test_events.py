from spur.core.events import RelocationEvent


def test_relocation_event_stores_relocation_data():
    event = RelocationEvent(
        content_name="video_001.mp4",
        previous_path="/programacao/dia_01/video_001.mp4",
        current_path="/programacao/dia_02/video_001.mp4"
    )

    assert event.content_name == "video_001.mp4"
    assert event.previous_path == "/programacao/dia_01/video_001.mp4"
    assert event.current_path == "/programacao/dia_02/video_001.mp4"