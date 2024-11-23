def hello(name,lan):
    greeting={
        "English":"Hello",
        "Spanish":"Hola",
        "German":"Hallo"
    }
    msg=f"{greeting[lan]} {name}!"
    print(msg)

#.....................................
if __name__=='__main__':
    import argparse

    parser=argparse.ArgumentParser(
        description="Provide a personal greerting"
    )

    parser.add_argument(
        "-n","--name",metavar="name",required=True,help="the name of the person greeting"
    )
    parser.add_argument(
        "-l","--lan",metavar="Language",required=True,help="The language of greeting"
    )
    args=parser.parse_args()
#****************************************************


# msg=f"Hello {args.name}"
# print(msg)

hello(args.name, args.lan)

