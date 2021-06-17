p=int(input("Unesi parametar : "))


def even(start, stop):
    for eve in range(start,stop + 1, 2):
        yield eve

def odds(start, stop):
    for odd in range(start,stop , 2):
        yield odd

def main():
    even_values = [eve for eve in even(1,p)]
    print("Neparni",even_values)

    odd_values = [odd for odd in odds(0, p)]
    print("Parni",odd_values)

if __name__ == '__main__':
    main()

