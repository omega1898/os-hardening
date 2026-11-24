# os-hardening

Automated hardening for Linux-based platforms, built as a starting point for Navy SBIR topic **DON27BZ02-NV010, Automated Hardening for Cyber Secure Operating Systems** (DoW FY27 Release 2).

## The problem

Hardening a platform by hand is slow, and unmanned and autonomous systems often ship a general-purpose Linux distribution with far more services, packages and kernel features than the mission needs. Every unused piece is attack surface. The topic asks for a tool that finds which OS functions a platform actually uses, removes the rest, and configures what remains securely, without breaking required functions.

## Approach in plain terms

1. **Observe** the platform while it does its real job: which processes run, which services are enabled, which ports listen, which kernel modules load.
2. **Compare** that against everything installed and enabled.
3. **Plan** removals and secure settings for whatever was never used.
4. **Apply** the plan only after a human or a policy approves it, then re-run the mission workload to prove nothing required broke.
5. **Measure** the before and after: attack surface removed and configuration checks passed.

## Phase I scope

A conceptual architecture plus a demonstration on one representative open-source platform, showing a measurable improvement in security posture. See [docs/topic-summary.md](docs/topic-summary.md).

## Status

Skeleton only. The first vertical slice (observation snapshot in, hardening plan out, dry run) is sketched in [docs/architecture.md](docs/architecture.md) and stubbed in `src/`.

## How to run

```bash
python -m unittest discover -s tests -v   # run the placeholder tests
PYTHONPATH=src python -m os_hardening.cli --help
```

## Documentation

- [docs/topic-summary.md](docs/topic-summary.md): what the public topic asks for
- [docs/topic-qa.md](docs/topic-qa.md): posted topic Q&A, summarized
- [docs/references.md](docs/references.md): the topic's references, with links
- [docs/submission-requirements.md](docs/submission-requirements.md): dates, award size, official instructions
- [docs/architecture.md](docs/architecture.md): first vertical slice and design decisions
