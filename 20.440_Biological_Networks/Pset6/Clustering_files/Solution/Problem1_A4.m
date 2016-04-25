% define inputs
X = [0 2; 0 1; 1 2; 2.5 5; 3.1 5; 3.1 6; 4 2; 5 2; 5 0];
k = 2;
equation = distance('Euclidean');
disp(equation);

[c, centroids_list, dists2centroids] = kmeans_cluster(X, k, equation);

disp('cluster set');
disp(c);
disp('final centroids')
disp(centroids_list);
disp('distance_matrix_simplified');
disp(dists2centroids);


