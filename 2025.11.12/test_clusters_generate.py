from matplotlib import pyplot as plt
from numpy import array, savetxt

from pathlib import Path
from random import randrange, shuffle, uniform
from sys import path


XYRange = tuple[float, float, float, float]

def generate_clusters(
        cluster1_range: XYRange, 
        *clusters_ranges: XYRange, 
        min_vals: int = 20, 
        max_vals: int = 30
    ):
    """
    
    :param cluster1_range: кортеж из четырёх float объектов; первые два задают диапазон для оси X, вторые два задают диапазон для оси Y
    """
    clusters_ranges = cluster1_range, *clusters_ranges
    clusters = []
    for cluster_range in clusters_ranges:
        x1, x2, y1, y2 = cluster_range
        cluster = []
        for _ in range(randrange(min_vals, max_vals)):
            cluster.append((uniform(x1, x2), uniform(y1, y2)))
        clusters.append(cluster)

    data = sum(clusters, [])
    shuffle(data)
    return array(data)


if __name__ == '__main__':
    
    data1 = generate_clusters(
        (1.5, 4, 2.5, 4),
        (3, 5, -2, 0),
        (-1, 2, -0.25, 1.75),
    )
    data2 = generate_clusters(
        (1.5, 4, 1.25, 2.5),
        (2, 4.5, -1, 1),
        (-0.5, 2.5, -0.25, 1.75),
    ) 
    
    data3 = generate_clusters(
        (1, 4, 1, 4),      # Первый кластер - левый нижний
        (4, 9, 9, 4),      # Второй кластер - правый нижний
        (3, 7, 5, 8),      # Третий кластер - левый верхний
        (2, 9, 1, 6),
        (1, 8, 5, 2),
    )   
    
    fig = plt.figure(figsize=(6, 6))
    axs = fig.subplots()
    
    x, y = data3.T
    axs.scatter(x, y)
    
    plt.show()
    
    
    savetxt(
        fname=Path(path[0]) / 'test_clusters-mixed.csv', 
        X=data3, 
        fmt='%.1f', 
        delimiter=','
    )

