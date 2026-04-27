from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    {
        "name": "api_dtos.py",
        "metadata_url": "http://localhost:5002",
        "output_name": "api",
    },
    {
        "name": "hub_dtos.py",
        "metadata_url": "http://localhost:5001",
        "output_name": "hub",
    },
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync Python ServiceStack references for norbix-python.")
    parser.add_argument(
        "--update-only",
        action="store_true",
        help="Update existing *.dtos.py files in references/ by running `x python` in-place.",
    )
    args = parser.parse_args()

    out_dir = ROOT / "references"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.update_only:
        existing = sorted(out_dir.glob("*_dtos.py"))
        if not existing:
            raise FileNotFoundError(
                "No existing Python references found in references/. Run sync without --update-only first."
            )
        for file in existing:
            cmd = ["x", "python", str(file)]
            print(f"[sync-types] updating {file.name} with: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
    else:
        for target in TARGETS:
            output_path = out_dir / target["name"]
            cmd = ["x", "python", target["metadata_url"], target["output_name"]]
            print(f"[sync-types] generating {output_path.name} with: {' '.join(cmd)}")
            subprocess.run(cmd, check=True, cwd=out_dir)

    print("[sync-types] done")


if __name__ == "__main__":
    main()
