import id_impl as ids


def unique(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return False
    return True


def check_unique(l):
    if not unique(l):
        raise Exception("list is not unique!")
    return True


def same(correct, tested):
    if len(correct) != len(tested):
        return False
    correct = sorted(correct)
    tested = sorted(tested)
    for i in range(len(correct)):
        if correct[i] != tested[i]:
            return False
    return True


def check_same(correct, tested):
    if not same(correct, tested):
        raise Exception("lists are not the same!")
    return True


def test01():
    alloc = ids.AllocatorId(100)

    id1 = alloc.get()
    id2 = alloc.get()
    id3 = alloc.get()
    id4 = alloc.get()
    id5 = alloc.get()

    check_unique([id1, id2, id3, id4, id5])

    alives = alloc.get_alives()

    check_same([id1, id2, id3, id4, id5], alives)

    print("TEST 01 PASSED")


def test02():
    alloc = ids.AllocatorId(100)

    id1 = alloc.get()
    id2 = alloc.get()
    id3 = alloc.get()
    id4 = alloc.get()
    id5 = alloc.get()

    alloc.back(id3)
    alloc.back(id2)
    alloc.back(id1)
    alloc.back(id4)
    alloc.back(id5)

    alives = alloc.get_alives()

    check_same([], alives)

    print("TEST 02 PASSED")


def test03():
    alloc = ids.AllocatorId(100)

    id1 = alloc.get()
    id2 = alloc.get()
    id3 = alloc.get()
    id4 = alloc.get()
    id5 = alloc.get()

    alloc.back(id3)
    alloc.back(id1)
    alloc.back(id5)

    alives = alloc.get_alives()

    check_same([id2, id4], alives)

    print("TEST 03 PASSED")


test01()
test02()
test03()
