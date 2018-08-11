# encoding: utf-8

def lengthLongestPath(input):
    maxlen = 0
    pathlen = {0:0}
    print(input.splitlines())
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen,pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen


if __name__ == "__main__":

    str = "dir\n\tsubdir11\n\t\ttestfile.ext\n\tsubdir2\n\t\tfile.ext"
    print(lengthLongestPath(str))
