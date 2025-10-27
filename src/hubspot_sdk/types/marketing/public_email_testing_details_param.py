# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicEmailTestingDetailsParam"]


class PublicEmailTestingDetailsParam(TypedDict, total=False):
    ab_sample_size_default: Annotated[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        PropertyInfo(alias="abSampleSizeDefault"),
    ]
    """
    Version of the email that should be sent if there are too few recipients to
    conduct an AB test.
    """

    ab_sampling_default: Annotated[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        PropertyInfo(alias="abSamplingDefault"),
    ]
    """
    Version of the email that should be sent if the results are inconclusive after
    the test period, master or variant.
    """

    ab_status: Annotated[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        PropertyInfo(alias="abStatus"),
    ]
    """Status of the AB test."""

    ab_success_metric: Annotated[
        Literal["CLICKS_BY_OPENS", "CLICKS_BY_DELIVERED", "OPENS_BY_DELIVERED"], PropertyInfo(alias="abSuccessMetric")
    ]
    """Metric to determine the version that will be sent to the remaining contacts."""

    ab_test_percentage: Annotated[int, PropertyInfo(alias="abTestPercentage")]
    """The size of your test group."""

    hours_to_wait: Annotated[int, PropertyInfo(alias="hoursToWait")]
    """Time limit on gathering test results.

    After this time is up, the winning version will be sent to the remaining
    contacts.
    """

    is_ab_variation: Annotated[bool, PropertyInfo(alias="isAbVariation")]

    test_id: Annotated[str, PropertyInfo(alias="testId")]
    """The ID of the AB test."""
