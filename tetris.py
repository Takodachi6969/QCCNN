def load_data(size, classes):
    import numpy as np
    def rand():
        return np.random.rand()

    s_mode = np.array([[0, 0, 0], [0, 1, 1], [1, 1, 0]])
    # 行翻转
    s = np.array([s_mode, s_mode[::-1]])
    # 列翻转
    s = np.append(s, s[:, :, ::-1], axis=0)
    # 转置
    s = np.append(s, s.transpose(0, 2, 1), axis=0)

    l_mode_1 = np.array([[1, 1, 1], [1, 0, 0], [0, 0, 0]])
    l_1 = np.array([l_mode_1, l_mode_1[::-1]])
    l_1 = np.append(l_1, l_1[:, :, ::-1], axis=0)
    l_1 = np.append(l_1, l_1.transpose(0, 2, 1), axis=0)
    l_mode_2 = np.array([[0, 0, 0], [1, 1, 1], [1, 0, 0]])
    l_2 = np.array([l_mode_2, l_mode_2[::-1]])
    l_2 = np.append(l_2, l_2[:, :, ::-1], axis=0)
    l_2 = np.append(l_2, l_2.transpose(0, 2, 1), axis=0)
    l = np.append(l_1, l_2, axis=0)

    o_mode = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
    o = np.array([o_mode, o_mode[::-1]])
    o = np.append(o, o[:, :, ::-1], axis=0)

    t_mode_1 = np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]])
    t_1 = np.array([t_mode_1, t_mode_1[::-1]])
    t_1 = np.append(t_1, t_1.transpose(0, 2, 1), axis=0)
    t_mode_2 = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    t_2 = np.array([t_mode_2, t_mode_2[::-1]])
    t_2 = np.append(t_2, t_2.transpose(0, 2, 1), axis=0)
    t = np.append(t_1, t_2, axis=0)

    x_data = np.array([]).reshape(0, 3, 3)
    y_data = np.array([])

    for i in range(size):
        if classes == 4:
            randint = np.random.randint(1, 37)
            if 1 <= randint <= 8:
                label = 'S'
                mode = s[randint - 1]
            if 9 <= randint <= 24:
                label = 'L'
                mode = l[randint - 8 - 1]
            if 25 <= randint <= 28:
                label = 'O'
                mode = o[randint - 24 - 1]
            if 29 <= randint <= 36:
                label = 'T'
                mode = t[randint - 28 - 1]      
        elif classes == 2:
            randint = np.random.randint(1, 17)
            if 1 <= randint <= 8:
                label = 'S'
                mode = s[randint - 1]
            if 9 <= randint <= 16:
                label = 'T'
                mode = t[randint - 8 - 1]
        else:
            pass
        graph = [[[rand() * 0.3 + 0.7 if j == 1 else rand() * 0.1 for j in i] for i in mode]]
        x_data = np.append(x_data, graph, axis=0)
        y_data = np.append(y_data, label)

    return x_data, y_data
