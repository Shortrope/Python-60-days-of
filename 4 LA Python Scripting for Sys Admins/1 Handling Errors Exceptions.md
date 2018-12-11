# Exit Status

    import sys
    sys.exit(1)

# Exceptions

    try:
        f = open(args.filename)

    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(2)

    else:
        with f:
            'do stuff'

    finally:
        print("finally always runnes")


