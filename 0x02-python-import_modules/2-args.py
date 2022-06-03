#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_arg = len(argv)
    n = 1

    if num_arg == 1:
        print("{} arguments.".format(num_arg - 1))
    elif num_arg > 1:
        s = "" if num_arg == 2 else "s"
        print("{} argument{}:".format(num_arg - 1, s))

        while n < num_arg:
            print("{}: {}".format(n, argv[n]))
            n += 1
