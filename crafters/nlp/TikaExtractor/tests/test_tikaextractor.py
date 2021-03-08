from .. import TikaExtractor


def test_extraction_uri():
    tika_extractor = TikaExtractor()
    crafted_docs = tika_extractor.craft(['cats_are_awesome.pdf', 'cats_are_awesome.pdf'], [None, None])
    assert len(crafted_docs) == 2
    for crafted_doc in crafted_docs:
        assert len(crafted_doc['text']) > 20


def test_extraction_bytes():
    tika_extractor = TikaExtractor()
    with open('cats_are_awesome.pdf', 'rb') as pdf:
        input_bytes = pdf.read()
    crafted_docs = tika_extractor.craft([None, None], [input_bytes, input_bytes])
    assert len(crafted_docs) == 2
    for crafted_doc in crafted_docs:
        assert len(crafted_doc['text']) > 20
