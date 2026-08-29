from spur.core.content import Content


def test_content_stores_attributes():
    content = Content(
        name="video_001.mp4",
        path="/programacao/dia_01/video_001.mp4",
        size=500000
    )

    assert content.name == "video_001.mp4"
    assert content.path == "/programacao/dia_01/video_001.mp4"
    assert content.size == 500000