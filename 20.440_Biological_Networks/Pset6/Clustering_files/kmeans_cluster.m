%% K-means clustering function
function [c,centroids,dists2centroids] = kmeans_cluster(X,k,distFun)
% check inputs
disp('X');
disp(X);
disp('k');
disp(k);
disp('distFun');
disp(distFun);

% Cutoff criteria 
epsilon = 1e-7; % Some small value

% Initialize cutoff values
maxEpsilon = 100; % Set to some large value initially

% Get intiial centroids by randomly sampling input matrix
% Assumes clustering dimension is by rows
rand_vals = randperm(size(X, 1));
centroids = X(rand_vals(1:k), : ); 

centroids_new = []; % define new centroids

% Begin loop and continue until cutoffs met
while maxEpsilon > epsilon
    
    % check variables
    disp('epsilon');
    disp(epsilon);
    disp('maxEpsilon');
    disp(maxEpsilon);
    disp('rand_vals');
    disp(rand_vals);
    disp('centroids');
    disp(centroids);

    % Determine distances to current centroids 
    dist_matrix = zeros(k, size(X, 1)); % define distance matrix
    disp('dist_matrix');
    disp(dist_matrix); % working
    
    for cluster = 1: k % k inclusive
        for coordinate = 1: Xsize
            A = X(coordinate, 1:2);
            B = centroids(cluster, 1:2);
            dist_matrix(cluster, coordinate) = distFun(A, B);
            % dist_matrix(cluster, coordinate) = sqrt(sum((X(coordinate, 1:2) - centroids(cluster, 1:2)).^2));
        end
    end
    
    disp('dist_matrix'); 
    disp(dist_matrix); 
    
    % Get membership of observations to clusters based on distance 
    cluster_set = cell(k, 1);
    
    for coordinate = 1: Xsize
        search_space = dist_matrix( : , coordinate); % define search space as column
        minimum = min(search_space); % find minimum per column
        [r_id c_id] = ind2sub(size(search_space), find(search_space == minimum)); % find row id for minimum value
        cluster_set{r_id} = [cluster_set{r_id}; (X(coordinate, : ))]; % assign mimimum value to cluster_set{row_id}
    end
    
    disp('cluster_set'); 
    celldisp(cluster_set); % display clusters
    
    % Re-calculate centroids based on current assignments 
    for count = 1: k % for each cluster define new centroids
        cluster = cluster_set{count};
        centroids_new = [centroids_new; mean(cluster(1:end, 1)) mean(cluster(1:end, 2))]; % working   
    end
    
    disp('centroids_new');
    disp(centroids_new);
   
    % Compute change in centroids  
    dist_diff_matrix = []; % define distance difference matrix
    for count = 1: k % for each centroid; determine distance moved
        old = centroids(count, 1:2); % generate (x0 y0) and (x1 y1)
        new = centroids_new(count, 1:2);
        difference = distFun(new, old);
        % difference = sqrt(sum((new - old).^2));
        dist_diff_matrix = [dist_diff_matrix difference]; % find distance and populate dist_diff_matrix
    end

    disp('dist_diff_matrix');
    disp(dist_diff_matrix);
    
    % Update centroids to new ones
    centroids = centroids_new;
    
    disp('centroids');
    disp(centroids);
    disp('centroids_new');
    disp(centroids_new);
    
    % update epsilon cutoff value
    maxEpsilon = min(dist_diff_matrix);
    disp('maxEpsilon');
    disp(maxEpsilon);
    
end

