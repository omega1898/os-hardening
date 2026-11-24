"""Planner: decides what to disable from an observation snapshot.

Pure functions only, so the logic can be tested without a live target.
Input files are untrusted: names are treated as plain strings, never run.
"""


def build_hardening_plan(enabled_services, observed_services, keep_services):
    """Return a plan listing enabled services that were never observed in use.

    enabled_services: services enabled on the platform.
    observed_services: services seen running during the mission workload.
    keep_services: services that must never be disabled (policy keep-list).
    """
    enabled_set = set(enabled_services)
    used_set = set(observed_services) | set(keep_services)
    services_to_disable = sorted(enabled_set - used_set)
    return {
        "mode": "dry_run",
        "disable_services": services_to_disable,
        "kept_services": sorted(enabled_set & used_set),
    }
