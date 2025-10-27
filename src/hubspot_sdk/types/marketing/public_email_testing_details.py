# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicEmailTestingDetails"]


class PublicEmailTestingDetails(BaseModel):
    ab_sample_size_default: Optional[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ]
    ] = FieldInfo(alias="abSampleSizeDefault", default=None)
    """
    Version of the email that should be sent if there are too few recipients to
    conduct an AB test.
    """

    ab_sampling_default: Optional[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ]
    ] = FieldInfo(alias="abSamplingDefault", default=None)
    """
    Version of the email that should be sent if the results are inconclusive after
    the test period, master or variant.
    """

    ab_status: Optional[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ]
    ] = FieldInfo(alias="abStatus", default=None)
    """Status of the AB test."""

    ab_success_metric: Optional[Literal["CLICKS_BY_OPENS", "CLICKS_BY_DELIVERED", "OPENS_BY_DELIVERED"]] = FieldInfo(
        alias="abSuccessMetric", default=None
    )
    """Metric to determine the version that will be sent to the remaining contacts."""

    ab_test_percentage: Optional[int] = FieldInfo(alias="abTestPercentage", default=None)
    """The size of your test group."""

    hours_to_wait: Optional[int] = FieldInfo(alias="hoursToWait", default=None)
    """Time limit on gathering test results.

    After this time is up, the winning version will be sent to the remaining
    contacts.
    """

    is_ab_variation: Optional[bool] = FieldInfo(alias="isAbVariation", default=None)

    test_id: Optional[str] = FieldInfo(alias="testId", default=None)
    """The ID of the AB test."""
