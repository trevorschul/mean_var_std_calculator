import numpy as np


def calculate(list):
    calculations = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "max": [],
        "min": [],
        "sum": [],

    }
    num_array = np.array([list[0:3], list[3:6], list[6:9]])
    calculations["mean"] = [
        [np.mean(num_array[:, 0]), np.mean(num_array[:, 1]), np.mean(num_array[:, 2])],
        [np.mean(num_array[0, :]), np.mean(num_array[1, :]), np.mean(num_array[2, :])],
        np.mean(list),
    ]
    calculations["variance"] = [
        [np.var(num_array[:, 0]), np.var(num_array[:, 1]), np.var(num_array[:, 2])],
        [np.var(num_array[0, :]), np.var(num_array[1, :]), np.var(num_array[2, :])],
        np.var(list),
    ]
    calculations["standard deviation"] = [
        [np.std(num_array[:, 0]), np.std(num_array[:, 1]), np.std(num_array[:, 2])],
        [np.std(num_array[0, :]), np.std(num_array[1, :]), np.std(num_array[2, :])],
        np.std(list),
    ]
    calculations["max"] = [
        [np.max(num_array[:, 0]), np.max(num_array[:, 1]), np.max(num_array[:, 2])],
        [np.max(num_array[0, :]), np.max(num_array[1, :]), np.max(num_array[2, :])],
        np.max(list),
    ]
    calculations["min"] = [
        [np.min(num_array[:, 0]), np.min(num_array[:, 1]), np.min(num_array[:, 2])],
        [np.min(num_array[0, :]), np.min(num_array[1, :]), np.min(num_array[2, :])],
        np.var(list),
    ]
    calculations["sum"] = [
        [np.sum(num_array[:, 0]), np.sum(num_array[:, 1]), np.sum(num_array[:, 2])],
        [np.sum(num_array[0, :]), np.sum(num_array[1, :]), np.sum(num_array[2, :])],
        np.sum(list),
    ]

    return calculations
