% define inputs
X = [0 2; 0 1; 1 2; 2.5 5; 3.1 5; 3.1 6; 4 2; 5 2; 5 0];
k = 2;
equation = distance('Euclidean');
disp(equation);

[c, centroids_list, dists2centroids] = kmeans_cluster(X, k, equation);

disp(c);
disp(centroids_list);
disp(dists2centroids);

% Assign final membership, centroids, and distances to centroids
