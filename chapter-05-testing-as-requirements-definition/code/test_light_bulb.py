from wiki import page_text


def test_light_bulb_page_mentions_edison():
    assert "Edison" in page_text("Incandescent_light_bulb")
