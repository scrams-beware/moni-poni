# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: RecipeCost
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="RecipeCost calculator")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("cost", help="Calculate recipe cost")
    p.add_argument("recipe", help="Recipe name")
    p.add_argument("-p", "--portions", type=int, default=1, help="Number of portions")
    p.add_argument("--ingredients", help="Comma-separated: name:weight,unit,cost_per_unit")
    p.add_argument("--prices", help="JSON prices: {\"ingredient\": price}")
    p.add_argument("--output", "-o", help="Output file (default: stdout)")

    p = sub.add_parser("report", help="Print summary report")
    p.add_argument("--output", "-o", help="Output file (default: stdout)")

    p = sub.add_parser("init", help="Initialize default data")
    p.add_argument("--output", "-o", help="Output file (default: stdout)")

    args = parser.parse_args()
    return args.command, getattr(args, "recipe", None), getattr(args, "portions", 1), getattr(args, "ingredients", None), getattr(args, "prices", None), getattr(args, "output", None)
