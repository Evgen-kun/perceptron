import random


def init_weights(ans, sl):
    return [[random.uniform(-1, 1) for j in range(sl)] for i in range(ans)]


def mat_mul(a, b):
    return [sum([a[k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))]


def sub_vec(a, b):
    return [a[i]-b[i] for i in range(len(a))]


def vec_mul_tr(a, b):
    return [[a_i * b_j for b_j in b] for a_i in a]


def const_mat_mul(a, b):
    return [[a * b_ij for b_ij in b_j] for b_j in b]


def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]



def hewiside(x):
    return [0 if x[i] <= 0 else 1 for i in range(len(x))]


def main():
    print('Введите количество эпох :')
    n = int(input())
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines.pop(0)
        lines = [[float(a) for a in l.split()] for l in lines]
        print(lines)
    weights = init_weights(len(lines[0])-2, 2)
    print(weights)
    for i in range(n):
        # train(weights, lines, 0.01)
        error = 0
        for line in lines:
            Y = mat_mul(line[:-2], weights)
            Y = hewiside(Y)
            delta = sub_vec(line[-2:], Y)
            error += max([abs(x) for x in delta])
            weights = add_matrix(weights, const_mat_mul(0.01, vec_mul_tr(line[:-2], delta)))
        print(error)
    with open('weights.txt', 'w') as f:
        f.write(str(weights))


if __name__ == '__main__':
    main()
