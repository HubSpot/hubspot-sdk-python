# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.data_studio import (
    DataSourceGetResponse,
    DataSourceUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasource:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        datasource = client.data_studio.datasource.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )
        assert datasource.is_closed
        assert datasource.json() == {"foo": "bar"}
        assert cast(Any, datasource.is_closed) is True
        assert isinstance(datasource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        datasource = client.data_studio.datasource.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                    "parent": {
                        "body_parts": [],
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    },
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                        "parent": {
                            "body_parts": [
                                {
                                    "content_disposition": {
                                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "file_name": "fileName",
                                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "parameters": {"foo": "string"},
                                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "size": 0,
                                        "type": "type",
                                    },
                                    "entity": {},
                                    "headers": {"foo": ["string"]},
                                    "media_type": {
                                        "parameters": {"foo": "string"},
                                        "subtype": "subtype",
                                        "type": "type",
                                        "wildcard_subtype": True,
                                        "wildcard_type": True,
                                    },
                                    "message_body_workers": {},
                                    "parameterized_headers": {
                                        "foo": [
                                            {
                                                "parameters": {"foo": "string"},
                                                "value": "value",
                                            }
                                        ]
                                    },
                                    "providers": {},
                                }
                            ],
                            "content_disposition": {
                                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "file_name": "fileName",
                                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "parameters": {"foo": "string"},
                                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "size": 0,
                                "type": "type",
                            },
                            "entity": {},
                            "headers": {"foo": ["string"]},
                            "media_type": {
                                "parameters": {"foo": "string"},
                                "subtype": "subtype",
                                "type": "type",
                                "wildcard_subtype": True,
                                "wildcard_type": True,
                            },
                            "message_body_workers": {},
                            "parameterized_headers": {
                                "foo": [
                                    {
                                        "parameters": {"foo": "string"},
                                        "value": "value",
                                    }
                                ]
                            },
                            "providers": {},
                        },
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
            parent={
                "body_parts": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    }
                ],
                "content_disposition": {
                    "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "file_name": "fileName",
                    "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "parameters": {"foo": "string"},
                    "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "size": 0,
                    "type": "type",
                },
                "entity": {},
                "headers": {"foo": ["string"]},
                "media_type": {
                    "parameters": {"foo": "string"},
                    "subtype": "subtype",
                    "type": "type",
                    "wildcard_subtype": True,
                    "wildcard_type": True,
                },
                "message_body_workers": {},
                "parameterized_headers": {
                    "foo": [
                        {
                            "parameters": {"foo": "string"},
                            "value": "value",
                        }
                    ]
                },
                "providers": {},
            },
        )
        assert datasource.is_closed
        assert datasource.json() == {"foo": "bar"}
        assert cast(Any, datasource.is_closed) is True
        assert isinstance(datasource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        datasource = client.data_studio.datasource.with_raw_response.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )

        assert datasource.is_closed is True
        assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert datasource.json() == {"foo": "bar"}
        assert isinstance(datasource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data_studio.datasource.with_streaming_response.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        ) as datasource:
            assert not datasource.is_closed
            assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert datasource.json() == {"foo": "bar"}
            assert cast(Any, datasource.is_closed) is True
            assert isinstance(datasource, StreamedBinaryAPIResponse)

        assert cast(Any, datasource.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        datasource = client.data_studio.datasource.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )
        assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        datasource = client.data_studio.datasource.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                    "parent": {
                        "body_parts": [],
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    },
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                        "parent": {
                            "body_parts": [
                                {
                                    "content_disposition": {
                                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "file_name": "fileName",
                                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "parameters": {"foo": "string"},
                                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "size": 0,
                                        "type": "type",
                                    },
                                    "entity": {},
                                    "headers": {"foo": ["string"]},
                                    "media_type": {
                                        "parameters": {"foo": "string"},
                                        "subtype": "subtype",
                                        "type": "type",
                                        "wildcard_subtype": True,
                                        "wildcard_type": True,
                                    },
                                    "message_body_workers": {},
                                    "parameterized_headers": {
                                        "foo": [
                                            {
                                                "parameters": {"foo": "string"},
                                                "value": "value",
                                            }
                                        ]
                                    },
                                    "providers": {},
                                }
                            ],
                            "content_disposition": {
                                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "file_name": "fileName",
                                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "parameters": {"foo": "string"},
                                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "size": 0,
                                "type": "type",
                            },
                            "entity": {},
                            "headers": {"foo": ["string"]},
                            "media_type": {
                                "parameters": {"foo": "string"},
                                "subtype": "subtype",
                                "type": "type",
                                "wildcard_subtype": True,
                                "wildcard_type": True,
                            },
                            "message_body_workers": {},
                            "parameterized_headers": {
                                "foo": [
                                    {
                                        "parameters": {"foo": "string"},
                                        "value": "value",
                                    }
                                ]
                            },
                            "providers": {},
                        },
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
            parent={
                "body_parts": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    }
                ],
                "content_disposition": {
                    "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "file_name": "fileName",
                    "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "parameters": {"foo": "string"},
                    "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "size": 0,
                    "type": "type",
                },
                "entity": {},
                "headers": {"foo": ["string"]},
                "media_type": {
                    "parameters": {"foo": "string"},
                    "subtype": "subtype",
                    "type": "type",
                    "wildcard_subtype": True,
                    "wildcard_type": True,
                },
                "message_body_workers": {},
                "parameterized_headers": {
                    "foo": [
                        {
                            "parameters": {"foo": "string"},
                            "value": "value",
                        }
                    ]
                },
                "providers": {},
            },
        )
        assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.data_studio.datasource.with_raw_response.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.data_studio.datasource.with_streaming_response.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.delete("/data-studio/2026-03/data-source/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        datasource = client.data_studio.datasource.delete(
            0,
        )
        assert datasource.is_closed
        assert datasource.json() == {"foo": "bar"}
        assert cast(Any, datasource.is_closed) is True
        assert isinstance(datasource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.delete("/data-studio/2026-03/data-source/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        datasource = client.data_studio.datasource.with_raw_response.delete(
            0,
        )

        assert datasource.is_closed is True
        assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert datasource.json() == {"foo": "bar"}
        assert isinstance(datasource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.delete("/data-studio/2026-03/data-source/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.data_studio.datasource.with_streaming_response.delete(
            0,
        ) as datasource:
            assert not datasource.is_closed
            assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert datasource.json() == {"foo": "bar"}
            assert cast(Any, datasource.is_closed) is True
            assert isinstance(datasource, StreamedBinaryAPIResponse)

        assert cast(Any, datasource.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        datasource = client.data_studio.datasource.get(
            0,
        )
        assert_matches_type(DataSourceGetResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.data_studio.datasource.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(DataSourceGetResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.data_studio.datasource.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(DataSourceGetResponse, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasource:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        datasource = await async_client.data_studio.datasource.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )
        assert datasource.is_closed
        assert await datasource.json() == {"foo": "bar"}
        assert cast(Any, datasource.is_closed) is True
        assert isinstance(datasource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        datasource = await async_client.data_studio.datasource.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                    "parent": {
                        "body_parts": [],
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    },
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                        "parent": {
                            "body_parts": [
                                {
                                    "content_disposition": {
                                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "file_name": "fileName",
                                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "parameters": {"foo": "string"},
                                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "size": 0,
                                        "type": "type",
                                    },
                                    "entity": {},
                                    "headers": {"foo": ["string"]},
                                    "media_type": {
                                        "parameters": {"foo": "string"},
                                        "subtype": "subtype",
                                        "type": "type",
                                        "wildcard_subtype": True,
                                        "wildcard_type": True,
                                    },
                                    "message_body_workers": {},
                                    "parameterized_headers": {
                                        "foo": [
                                            {
                                                "parameters": {"foo": "string"},
                                                "value": "value",
                                            }
                                        ]
                                    },
                                    "providers": {},
                                }
                            ],
                            "content_disposition": {
                                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "file_name": "fileName",
                                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "parameters": {"foo": "string"},
                                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "size": 0,
                                "type": "type",
                            },
                            "entity": {},
                            "headers": {"foo": ["string"]},
                            "media_type": {
                                "parameters": {"foo": "string"},
                                "subtype": "subtype",
                                "type": "type",
                                "wildcard_subtype": True,
                                "wildcard_type": True,
                            },
                            "message_body_workers": {},
                            "parameterized_headers": {
                                "foo": [
                                    {
                                        "parameters": {"foo": "string"},
                                        "value": "value",
                                    }
                                ]
                            },
                            "providers": {},
                        },
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
            parent={
                "body_parts": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    }
                ],
                "content_disposition": {
                    "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "file_name": "fileName",
                    "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "parameters": {"foo": "string"},
                    "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "size": 0,
                    "type": "type",
                },
                "entity": {},
                "headers": {"foo": ["string"]},
                "media_type": {
                    "parameters": {"foo": "string"},
                    "subtype": "subtype",
                    "type": "type",
                    "wildcard_subtype": True,
                    "wildcard_type": True,
                },
                "message_body_workers": {},
                "parameterized_headers": {
                    "foo": [
                        {
                            "parameters": {"foo": "string"},
                            "value": "value",
                        }
                    ]
                },
                "providers": {},
            },
        )
        assert datasource.is_closed
        assert await datasource.json() == {"foo": "bar"}
        assert cast(Any, datasource.is_closed) is True
        assert isinstance(datasource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        datasource = await async_client.data_studio.datasource.with_raw_response.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )

        assert datasource.is_closed is True
        assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await datasource.json() == {"foo": "bar"}
        assert isinstance(datasource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/data-studio/2026-03/data-source").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data_studio.datasource.with_streaming_response.create(
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        ) as datasource:
            assert not datasource.is_closed
            assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await datasource.json() == {"foo": "bar"}
            assert cast(Any, datasource.is_closed) is True
            assert isinstance(datasource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, datasource.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        datasource = await async_client.data_studio.datasource.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )
        assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        datasource = await async_client.data_studio.datasource.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                    "parent": {
                        "body_parts": [],
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    },
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                        "parent": {
                            "body_parts": [
                                {
                                    "content_disposition": {
                                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "file_name": "fileName",
                                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "parameters": {"foo": "string"},
                                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                        "size": 0,
                                        "type": "type",
                                    },
                                    "entity": {},
                                    "headers": {"foo": ["string"]},
                                    "media_type": {
                                        "parameters": {"foo": "string"},
                                        "subtype": "subtype",
                                        "type": "type",
                                        "wildcard_subtype": True,
                                        "wildcard_type": True,
                                    },
                                    "message_body_workers": {},
                                    "parameterized_headers": {
                                        "foo": [
                                            {
                                                "parameters": {"foo": "string"},
                                                "value": "value",
                                            }
                                        ]
                                    },
                                    "providers": {},
                                }
                            ],
                            "content_disposition": {
                                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "file_name": "fileName",
                                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "parameters": {"foo": "string"},
                                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "size": 0,
                                "type": "type",
                            },
                            "entity": {},
                            "headers": {"foo": ["string"]},
                            "media_type": {
                                "parameters": {"foo": "string"},
                                "subtype": "subtype",
                                "type": "type",
                                "wildcard_subtype": True,
                                "wildcard_type": True,
                            },
                            "message_body_workers": {},
                            "parameterized_headers": {
                                "foo": [
                                    {
                                        "parameters": {"foo": "string"},
                                        "value": "value",
                                    }
                                ]
                            },
                            "providers": {},
                        },
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
            parent={
                "body_parts": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                    }
                ],
                "content_disposition": {
                    "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "file_name": "fileName",
                    "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "parameters": {"foo": "string"},
                    "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "size": 0,
                    "type": "type",
                },
                "entity": {},
                "headers": {"foo": ["string"]},
                "media_type": {
                    "parameters": {"foo": "string"},
                    "subtype": "subtype",
                    "type": "type",
                    "wildcard_subtype": True,
                    "wildcard_type": True,
                },
                "message_body_workers": {},
                "parameterized_headers": {
                    "foo": [
                        {
                            "parameters": {"foo": "string"},
                            "value": "value",
                        }
                    ]
                },
                "providers": {},
            },
        )
        assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.data_studio.datasource.with_raw_response.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.data_studio.datasource.with_streaming_response.update(
            datasource_id=0,
            body_parts=[
                {
                    "content_disposition": {
                        "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "file_name": "fileName",
                        "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "parameters": {"foo": "string"},
                        "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "size": 0,
                        "type": "type",
                    },
                    "entity": {},
                    "headers": {"foo": ["string"]},
                    "media_type": {
                        "parameters": {"foo": "string"},
                        "subtype": "subtype",
                        "type": "type",
                        "wildcard_subtype": True,
                        "wildcard_type": True,
                    },
                    "message_body_workers": {},
                    "parameterized_headers": {
                        "foo": [
                            {
                                "parameters": {"foo": "string"},
                                "value": "value",
                            }
                        ]
                    },
                    "providers": {},
                }
            ],
            content_disposition={
                "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "file_name": "fileName",
                "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parameters": {"foo": "string"},
                "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "size": 0,
                "type": "type",
            },
            entity={},
            fields={
                "foo": [
                    {
                        "content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "entity": {},
                        "form_data_content_disposition": {
                            "creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "file_name": "fileName",
                            "modification_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "name": "name",
                            "parameters": {"foo": "string"},
                            "read_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "size": 0,
                            "type": "type",
                        },
                        "headers": {"foo": ["string"]},
                        "media_type": {
                            "parameters": {"foo": "string"},
                            "subtype": "subtype",
                            "type": "type",
                            "wildcard_subtype": True,
                            "wildcard_type": True,
                        },
                        "message_body_workers": {},
                        "name": "name",
                        "parameterized_headers": {
                            "foo": [
                                {
                                    "parameters": {"foo": "string"},
                                    "value": "value",
                                }
                            ]
                        },
                        "providers": {},
                        "simple": True,
                        "value": "value",
                    }
                ]
            },
            headers={"foo": ["string"]},
            media_type={
                "parameters": {"foo": "string"},
                "subtype": "subtype",
                "type": "type",
                "wildcard_subtype": True,
                "wildcard_type": True,
            },
            message_body_workers={},
            parameterized_headers={
                "foo": [
                    {
                        "parameters": {"foo": "string"},
                        "value": "value",
                    }
                ]
            },
            providers={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(DataSourceUpdateResponse, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.delete("/data-studio/2026-03/data-source/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        datasource = await async_client.data_studio.datasource.delete(
            0,
        )
        assert datasource.is_closed
        assert await datasource.json() == {"foo": "bar"}
        assert cast(Any, datasource.is_closed) is True
        assert isinstance(datasource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.delete("/data-studio/2026-03/data-source/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        datasource = await async_client.data_studio.datasource.with_raw_response.delete(
            0,
        )

        assert datasource.is_closed is True
        assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await datasource.json() == {"foo": "bar"}
        assert isinstance(datasource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.delete("/data-studio/2026-03/data-source/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.data_studio.datasource.with_streaming_response.delete(
            0,
        ) as datasource:
            assert not datasource.is_closed
            assert datasource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await datasource.json() == {"foo": "bar"}
            assert cast(Any, datasource.is_closed) is True
            assert isinstance(datasource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, datasource.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        datasource = await async_client.data_studio.datasource.get(
            0,
        )
        assert_matches_type(DataSourceGetResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.data_studio.datasource.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(DataSourceGetResponse, datasource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.data_studio.datasource.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(DataSourceGetResponse, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True
