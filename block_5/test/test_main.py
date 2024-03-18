import pytest
from contextlib import nullcontext as ex_not_raise
from block_5.src.main import ApiRequest


class TestApiRequest:
    @pytest.mark.parametrize(
        ["type", "payload", "res", "expect"],
        [
            ('GET', {"key": "value"}, 'GET', pytest.raises(AttributeError)),
            ('GET', None, 'GET', ex_not_raise()),
            ('Get', {"key": "value"}, 'Get', pytest.raises(TypeError)),
            ('POST', {"hidden_key": "hidden_value"}, 'POST', ex_not_raise()),
            ('NEPOST', {"hidden_key": "hidden_value"}, 'NEPOST', pytest.raises(TypeError)),
        ]
    )
    def test_type_ApiRequest(self, type, payload, res, expect):
        with expect:
            assert ApiRequest(payload=payload, request_type=type).get_type() == res

    @pytest.mark.parametrize(
        ["type", "payload", "res", "ex"],
        [
            ('GET', {"key": "value"}, {"key": "value"}, pytest.raises(AttributeError)),
            ('GET', None, None, ex_not_raise()),
            ('Get', {"key": "value"}, 'Get', pytest.raises(TypeError)),
            ('POST', {"hidden_key": "hidden_value"}, {"hidden_key": "hidden_value"}, ex_not_raise()),
            ('NEPOST', {"hidden_key": "hidden_value"}, 'NEPOST', pytest.raises(TypeError)),
        ]
    )
    def test_get_payload_ApiRequest(self, type, payload, res, ex):
        with ex:
            assert ApiRequest(payload=payload, request_type=type).get_payload() == res

    @pytest.mark.parametrize(
        ["type", "payload", "new_payload", "res", "ex"],
        [
            ('GET', {"key": "value"}, {"new_key": "new_value"}, {"new_key": "new_value"}, pytest.raises(AttributeError)),
            ('GET', None, {"new_key": "new_value"}, None, pytest.raises(AttributeError)),
            ('Get', {"key": "value"}, {"new_key": "new_value"}, {"new_key": "new_value"}, pytest.raises(TypeError)),
            ('POST', {"hidden_key": "hidden_value"}, {"new_hidden_key": "new_hidden_value"}, {"new_hidden_key": "new_hidden_value"}, ex_not_raise()),
            ('NEPOST', {"hidden_key": "hidden_value"}, {"new_hidden_key": "new_hidden_value"}, {"new_hidden_key": "new_hidden_value"}, pytest.raises(TypeError)),
        ]
    )
    def test_set_payload_ApiRequest(self, type, payload, new_payload, res, ex):
        with ex:
            assert ApiRequest(payload=payload, request_type=type).set_payload(new_payload) == res

