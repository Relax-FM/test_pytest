import pytest
from contextlib import nullcontext as ex_not_raise
from block_5.src.main import ApiRequest


class TestApiRequest:
    @pytest.mark.parametrize(
        "type, payload, res, ex",
        ('GET', 'payload', 'GET', ex_not_raise()),
        ('Get', 'payload', 'Get', pytest.raises(TypeError)),
        ('POST', 'hidden payload', 'POST', ex_not_raise()),
        ('NEPOST', 'hidden payload', 'NEPOST', pytest.raises(TypeError)),
    )
    def test_type_ApiRequest(self, type, payload, res, ex):
        api = ApiRequest()
        with ex:


    @pytest.mark.parametrize(
        "type, payload, ex",
        ()
    )
    def test_payload_ApiRequest(self):
        pass

    @pytest.mark.parametrize(
        "type, payload, ex",
        ()
    )
    def test_set_payload_ApiRequest(self):
        pass
