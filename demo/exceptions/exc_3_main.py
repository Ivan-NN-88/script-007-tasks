import sys

if __name__ == '__main__':
    try:

        # main()
        pass

    except KeyboardInterrupt:
        print(f'\nERROR: Interrupted by user', file=sys.stderr)
        sys.exit(1)
    except BaseException as err:
        print(f'ERROR: Something goes wrong:\n{err}', file=sys.stderr)
        sys.exit(1)
