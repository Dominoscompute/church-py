def main():
    import lib
    def uncons(xs):
        return (xs[0],xs[1:])
    print(lib.ch2num(lib.zero))
    print(lib.to_list(1,2))
    print(lib.ch2num(lib.pred(lib.one_hundred)))
if __name__ == "__main__":
    main()
