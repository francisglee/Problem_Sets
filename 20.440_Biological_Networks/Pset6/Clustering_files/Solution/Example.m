k = 3;
cluster_set = cell(k, 1);

celldisp(cluster_set);

Xsize = 9;
X = [0 2; 0 1; 1 2; 2.5 5; 3.1 5; 3.1 6; 4 2; 5 2; 5 0];
dist_matrix = zeros(k, Xsize);
centroids = [ 3.1000 5.0000; 0 1.0000; 1.0000 2.0000];

for cluster = 1: k % k inclusive
    for coordinate = 1: Xsize
        dist_matrix(cluster, coordinate) = sqrt(sum((X(coordinate, 1:2) - centroids(cluster, 1:2)).^2));
    end
end

disp(dist_matrix);

for coordinate = 1: Xsize
    search_space = dist_matrix( : , coordinate); % define search space as column
    disp(search_space);
    minimum = min(search_space); % find minimum per column
    disp(minimum);
    [r_id c_id] = ind2sub(size(search_space), find(search_space == minimum)); % find row id for minimum value
    if size(r_id, 1) > 1
        r_ida = r_id(1);
        cluster_set{r_ida} = [cluster_set{r_ida}; (X(coordinate, : ))]; % assign mimimum value to cluster_set{row_id}
    else
        cluster_set{r_id} = [cluster_set{r_id}; (X(coordinate, : ))]; % assign mimimum value to cluster_set{row_id}
    end
end

celldisp(cluster_set);
