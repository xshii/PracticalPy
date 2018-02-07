# demo
# python argument.py --sum 1 2 3 4  #   10
# python argument.py 1 2 3 4        #   4

import argparse

# argparse.ArgumentParser()

VERSION_NUM = '0.0.1'

# Create a New ArgumentParser Object
parser = argparse.ArgumentParser(prog="Integers Processor Version:{}".format(VERSION_NUM), description='Sum up or get the max value of some integers.')
"""Object for parsing command line strings into Python objects.

    Keyword Arguments:
        - prog=None:         String -- The name of the program (default: sys.argv[0])
        - usage=None:        String -- A usage message (default: auto-generated from arguments)
        - description=None:  String -- A description of what the program does
        - epilog=None:       String -- Text following the argument descriptions
        - parents=[]:               -- Parsers whose arguments should be copied into this one
        - formatter_class=argparse.HelpFormatter 
                                    -- HelpFormatter class for printing help messages
        - prefix_chars='-'          -- Characters that is allowed to prefix optional arguments
        - fromfile_prefix_chars=None-- Characters that prefix files containing additional arguments '@args.txt'
        - argument_default=None     -- The default value for all arguments
        - conflict_handler='error'  -- String indicating how to handle conflicts
        - add_help=True             -- Add a -h/-help option            @ set False for parents parser 
        - allow_abbrev=True         -- Allow long options to be abbreviated unambiguously @ invalid if args share same head characters
    
    
    # Corresponding output
    usage: <prog> [argument list] / <usage> |
                                            }   argparse.RawDescriptionHelpFormatter
    <description>                           |
    
    optional arguments:
    -h, --help   show this help message and exit
    <argument>  ...                         }   argparse.MetavarTypeHelpFormatter will use `type` rather than `dest`
    
    <epilog>
    
"""



# Add additional argument
# --help and -h are default.
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator', choices=range(1,10))
parser.add_argument('--sum', '-s', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
"""Add arguments
    Keyword Arguments:
    name or flag:...String  - Either a name or a list of option strings @ with `-` optional argument
                                                                        @ without `-` positional argument
    action: The basic type of action to be taken when this argument is encountered at the command line.
                                                                        @ `store` default
                                                                        @ `store_const` store values by `const`
                                                                        @ `store_true`, ```store_false```, store default t or f
                                                                        @ `append`, multiple times options
                                                                        @ `append_const` 
                                                                        @ `count` count the times of options appear
                                                                        @ `help`,`version`,
                                                                        @ custom Action
    nargs:  The number of command-line arguments that should be consumed.
                                                                        @ `N` gather into a list
                                                                        @ `?` check `const` then `default`
                                                                        @ '*' gather into a list can be empty
                                                                        @ '+' gather into a non-empty list
                                                                        @ argparse.REMAINDER 
    const: A constant value required by some action and nargs selections.
                                                                        @ a constant or a callable
    default: The value produced if the argument is absent from the command line.
                                                                        @ a constant or a callable
    type: The type to which the command-line argument should be converted.
                                                                        @ a constant or a callable
                                                                        @ argparse.FileType('w') to create a writable file
    choices: A container of the allowable values for the argument.      @ a list of values
    required=False: Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A display name for the argument in usage messages.                @ better for the position argument.
    dest - The name of the attribute to be added to the object returned by parse_args().
"""

args = parser.parse_args()
print(args.accumulate(args.integers))


# .add_subparser?
# .add_argument_group()
# .set_defaults(**kwargs)
# .get_default(dest)
parser.set_defaults(sum='max')
print(parser.get_default('sum'))

# print help
# .print_usage(file=None)
# .print_help(file=None)
# .format_usage()
# .format_help()

# exit
# .exit(status=0, message=None)
# .error(message)   @ status = 2