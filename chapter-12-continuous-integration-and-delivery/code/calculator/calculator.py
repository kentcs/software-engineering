"""Small addition calculator adapted from the earlier testing exercise."""
import argparse


def add(left, right):
    return left + right


def main():
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    args = parser.parse_args()
    print(add(args.left, args.right))


if __name__ == "__main__":
    main()
