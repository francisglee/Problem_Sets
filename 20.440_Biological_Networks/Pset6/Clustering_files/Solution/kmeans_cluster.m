%% K-means clustering function
function [c, centroids_final, dists2centroids] = kmeans_cluster(X, k, distFun)

%{
% check inputs
disp('X');
disp(X);
disp('k');
disp(k);
disp('distFun');
disp(distFun);
%}

% Cutoff criteria 
epsilon = 1e-7; % Some small value

% Initialize cutoff values
maxEpsilon = 100; % Set to some large value initially

% Get intiial centroids by randomly sampling input matrix
% Assumes clustering dimension is by rows
rand_vals = randperm(size(X, 1));
% rand_vals = [6 4 7 9 3 2 8 5 1]; % just for testing
centroids = X(rand_vals(1:k), : ); 
% centroids = [1 2; 5 2]; % just for testing

%{
disp('rand_vals');
disp(rand_vals);
%}

centroids_new = zeros(k, 2); % define new centroids
Xsize = size(X, 1); % define size of dataset
dist_matrix = zeros(k, Xsize); % define distance matrix of each observation to centroid
dist_matrix_simplified = zeros(1, Xsize); % define distance of observation to it's centroid
cluster_set_matrix = zeros(k, 1); % define cluster set matrix 
cluster_set = cell(k, 1); % group observations into clusters
dist_diff_matrix = zeros(1, k); % define matrix distance differential between old and new centroids  
cluster_iteration_counter = 0; 

% Begin loop and continue until cutoffs met
while maxEpsilon > epsilon
    
    %{
    % check variables
    disp('epsilon');
    disp(epsilon);
    disp('maxEpsilon');
    disp(maxEpsilon);  
    disp('centroids');
    disp(centroids);
    %}
    
    %{
    % Determine distances to current centroids 
    disp('initial dist_matrix'); 
    disp(dist_matrix); 
    disp('initial dist_matrix_simplified'); 
    disp(dist_matrix_simplified); % display distances
    %}
    
    for cluster = 1: k % k inclusive
        for coordinate = 1: Xsize
            A = X(coordinate, 1:2);
            B = centroids(cluster, 1:2);
            dist_matrix(cluster, coordinate) = distFun(A, B);
            % dist_matrix(cluster, coordinate) = sqrt(sum((X(coordinate, 1:2) - centroids(cluster, 1:2)).^2));
        end
    end
    
    %{
    disp('dist_matrix');
    disp(dist_matrix); % working
    %}
    
    % Get membership of observations to clusters based on distance 
    for coordinate = 1: Xsize
        search_space = dist_matrix( : , coordinate); % define search space as column
        minimum = min(search_space); % find minimum per column
        [r_id c_id] = ind2sub(size(search_space), find(search_space == minimum)); % find row id for minimum value
        if size(r_id, 1) > 1
            r_ida = r_id(1);
            cluster_set{r_ida} = [cluster_set{r_ida}; (X(coordinate, : ))]; % assign FIRST mimimum value to cluster_set{row_id}
            cluster_set_matrix(coordinate) = r_ida; % assign FIRST mimimum value to cluster_set; all values should be non-zero
        else
            cluster_set{r_id} = [cluster_set{r_id}; (X(coordinate, : ))]; % assign mimimum value to cluster_set{row_id}
            cluster_set_matrix(coordinate) = r_id; % assign mimimum value to cluster_set; all values should be non-zero
        end
        dist_matrix_simplified(coordinate) = minimum; 
    end
    
    %{
    disp('cluster_set'); 
    celldisp(cluster_set); % display clusters
    disp('cluster_set_matrix'); 
    disp(cluster_set_matrix); % display clusters
    disp('dist_matrix_simplified'); 
    disp(dist_matrix_simplified); % display distances
    %}
    
    % Re-calculate centroids based on current assignments 
    % define new centroids

    for count = 1: k % for each cluster define new centroids
        cluster = cluster_set{count};
        if isempty(cluster)
            break
        else
            centroids_new(count, 1:2 ) = [mean(cluster(1:end, 1)) mean(cluster(1:end, 2))]; % working  
        end   
    end
    
    %{
    disp('centroids_new');
    disp(centroids_new);

    disp('centroids');
    disp(centroids);
    %}
    
    % Compute change in centroids  
    for count = 1: k % for each centroid; determine distance moved
        old = centroids(count, 1:2); % generate (x0 y0) and (x1 y1)
        new = centroids_new(count, 1:2);
        difference = distFun(new, old);
        % difference = sqrt(sum((new - old).^2));
        dist_diff_matrix(count) = difference; % find distance and populate dist_diff_matrix
    end
    
    %{
    disp('dist_diff_matrix');
    disp(dist_diff_matrix);
    %}
    
    % Update centroids to new ones
    centroids = centroids_new;
    
    %{
    disp('centroids_new');
    disp(centroids_new);
    disp('updated centroids should equal centroids_new');
    disp(centroids);
    %}
    
    % update epsilon cutoff value with max distance differential 
    maxEpsilon = max(dist_diff_matrix);
    %{
    disp('maxEpsilon');
    disp(maxEpsilon);
    %}
    cluster_set = cell(k, 1); % reinitialize cell array
    
    cluster_iteration_counter = cluster_iteration_counter + 1;
    
end % end while loop

% Assign final membership, centroids, and distances to centroids
%{
disp('Kmeans cluster iteration count: ');
disp(cluster_iteration_counter);
%}

c = cluster_set_matrix; % 1-D vector cluster assignments for each observation
centroids_final = centroids_new; % coordinates of centroid
dists2centroids = dist_matrix_simplified; % 1-D vector of distances of each observation to its calculated centroid

