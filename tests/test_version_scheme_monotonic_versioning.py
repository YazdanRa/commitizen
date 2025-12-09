from __future__ import annotations

import pytest

from commitizen.version_schemes import MonotonicVersion, VersionProtocol
from tests.utils import VersionSchemeTestArgs


@pytest.mark.parametrize(
    "version_args, expected_version",
    [
        (
            VersionSchemeTestArgs(
                current_version="1",
                increment="PATCH",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "2",
        ),
        (
            VersionSchemeTestArgs(
                current_version="2",
                increment="MINOR",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "3",
        ),
        (
            VersionSchemeTestArgs(
                current_version="3",
                increment="MAJOR",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "4",
        ),
        (
            VersionSchemeTestArgs(
                current_version="10",
                increment="PATCH",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "11",
        ),
    ],
)
def test_bump_monotonic_version(
    version_args: VersionSchemeTestArgs, expected_version: str
):
    assert (
        str(
            MonotonicVersion(version_args.current_version).bump(
                increment=version_args.increment,
                prerelease=version_args.prerelease,
                prerelease_offset=version_args.prerelease_offset,
                devrelease=version_args.devrelease,
            )
        )
        == expected_version
    )


def test_monotonic_scheme_property():
    version = MonotonicVersion("1")
    assert version.scheme is MonotonicVersion


def test_monotonic_implements_version_protocol():
    assert isinstance(MonotonicVersion("1"), VersionProtocol)
