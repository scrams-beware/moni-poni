# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: RecipeCost
import copy
from typing import Optional


def dry_run_mode() -> None:
    """Activate dry-run mode: all mutating operations are logged instead of executed."""
    global _dry_run
    _dry_run = True
    print("[INFO] Dry-run mode enabled. All writes will be logged and discarded.")


def disable_dry_run() -> None:
    """Deactivate dry-run mode."""
    global _dry_run
    _dry_run = False


def dry_run_context():
    """Context manager for temporary dry-run activation."""
    class DryRunContext:
        def __enter__(self):
            global _dry_run
            _dry_run = True
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            global _dry_run
            _dry_run = False
            return False

    return DryRunContext()


# Global flag to track dry-run state
_dry_run = False


def log_dry_run(operation, data=None):
    """Log an operation that would be performed in dry-run mode."""
    if _dry_run:
        print(f"[DRY-RUN] {operation}: {data}")
        return data
    return data
