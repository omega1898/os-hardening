import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from os_hardening.plan import build_hardening_plan


class BuildHardeningPlanTest(unittest.TestCase):
    def test_unused_enabled_service_is_planned_for_disable(self):
        plan = build_hardening_plan(
            enabled_services=["sshd", "cups", "avahi-daemon", "autonomy-stack"],
            observed_services=["autonomy-stack"],
            keep_services=["sshd"],
        )
        self.assertEqual(plan["disable_services"], ["avahi-daemon", "cups"])
        self.assertEqual(plan["mode"], "dry_run")


if __name__ == "__main__":
    unittest.main()
