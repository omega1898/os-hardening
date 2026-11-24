"""Command line entry point: snapshot JSON in, hardening plan JSON out."""
import argparse
import json

from os_hardening.plan import build_hardening_plan


def main(argument_list=None):
    parser = argparse.ArgumentParser(description="Build a dry-run hardening plan from a snapshot.")
    parser.add_argument("snapshot_path", help="JSON with enabled_services, observed_services, keep_services")
    arguments = parser.parse_args(argument_list)
    with open(arguments.snapshot_path, encoding="utf-8") as snapshot_file:
        snapshot = json.load(snapshot_file)
    plan = build_hardening_plan(
        snapshot.get("enabled_services", []),
        snapshot.get("observed_services", []),
        snapshot.get("keep_services", []),
    )
    print(json.dumps(plan, indent=2))


if __name__ == "__main__":
    main()
