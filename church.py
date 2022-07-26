def main():
    import lib
    def uncons(xs):
        return (xs[0],xs[1:])
    print(lib.ch2num(lib.zero))
    print(lib.ch2num(lib.pred(lib.one_hundred)))
    print(lib.ch2int(lib.smul(lib.ints(-3))(lib.ints(-23))))
if __name__ == "__main__":
    main()
