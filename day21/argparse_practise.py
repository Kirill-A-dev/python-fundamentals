import argparse
def create_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
    "command", 
    choices=["list", "status", "start", "stop"],
    help="Command to execute"
    )
    parser.add_argument(
    "service",
    nargs="?",
    help="Service name"
    )
        
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()


    if args.command == "list":
        print("List command: ")
    else:
        if args.service is None:
            parser.error("Service is required")
        else:
            print(args.service)

if __name__ == "__main__":
    main()