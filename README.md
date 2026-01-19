# LumenFlow Example: Python

Example Python project demonstrating [LumenFlow](https://lumenflow.dev) workflow setup.

## What is LumenFlow?

LumenFlow is a delivery framework for AI-native software development. It provides:

- **Work Units (WUs)**: Atomic units of work with clear acceptance criteria
- **Lanes**: Parallel delivery streams with WIP=1 enforcement
- **Gates**: Quality checks (format, lint, typecheck, test) that must pass
- **TDD-First**: Test-driven development with hexagonal architecture

## Quick Start

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
# Or with uv:
uv pip install -e ".[dev]"

# Run gates (format check, lint, typecheck, tests)
ruff format --check .
ruff check .
mypy src/
pytest
```

## Project Structure

```
.
├── .lumenflow.config.yaml    # LumenFlow configuration
├── .beacon/
│   └── stamps/               # WU completion stamps
├── docs/
│   └── 04-operations/
│       └── tasks/
│           ├── wu/           # Work Unit specs
│           ├── backlog.md    # Backlog of all WUs
│           └── status.md     # Current status board
├── src/
│   ├── __init__.py
│   └── calculator.py         # Application source
├── tests/
│   └── test_calculator.py    # Tests
└── pyproject.toml            # Project configuration
```

## Gates Configuration

This project uses the following quality gates:

| Gate | Tool | Command |
|------|------|---------|
| Format | Ruff Format | `ruff format --check .` |
| Lint | Ruff | `ruff check .` |
| Type Check | mypy | `mypy src/` |
| Test | pytest | `pytest` |

All gates must pass before a WU can be marked done.

## Working with WUs

### View the Backlog

See [docs/04-operations/tasks/backlog.md](docs/04-operations/tasks/backlog.md) for available work.

### Claim a WU

```bash
# With LumenFlow CLI installed:
pnpm wu:claim --id WU-001 --lane Core
cd worktrees/core-wu-001
```

### Complete a WU

```bash
# Run gates first
ruff format --check . && ruff check . && mypy src/ && pytest

# Return to main and complete
cd ../..
pnpm wu:done --id WU-001
```

## Documentation

- [LumenFlow Documentation](https://lumenflow.dev) - Complete framework reference
- [Getting Started](https://lumenflow.dev/getting-started/quickstart) - Quick start guide
- [Configuration Reference](https://lumenflow.dev/reference/config) - Config options
- [WU Schema](https://lumenflow.dev/reference/wu-schema) - Work Unit specification

## License

MIT
