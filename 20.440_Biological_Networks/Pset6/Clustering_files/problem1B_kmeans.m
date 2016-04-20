function problem1B_kmeans()

x = [0 2; 0 1; 1 2; 2.5 5; 3.1 5; 3.1 6; 4 2; 5 2; 5 0];
k = 2;

distance_matrix = [x];

for cluster = k
    for item = x
        distance_array = distFun(k, centroids(cluster));
        distance_matrix 
        
% distance matrix should look like...
% row one coordinates
% row two distances from centroid(1)

%% K-means clustering function
function [c,centroids,dists2centroids] = kmeans_cluster(X, k, distFun)
% Cutoff criteria 
epsilon = 1e-7; % Some small value

% Initialize cutoff values
maxEpsilon = 100; % Set to some large value initially

% Get intiial centroids by randomly sampling input matrix
% Assumes clustering dimension is by rows
rand_vals = randperm(size(X, 1));
centroids = X(rand_vals(1: k), : ); 

% Begin loop and continue until cutoffs met
while maxEpsilon > epsilon

    % Determine distances to current centroids
    dist_mat = 
    
    % Get membership of observations to clusters based on distance
    
    % Re-calculate centroids based on current assignments

    % Compute change in centroids
    
    % Update centroids to new ones
    
    % update epsilon cutoff value
    
end

% Assign final membership, centroids, and distances to centroids

%% Distance function
function fun = distance(dist)
switch dist
    case 'Euclidean'
        fun = @(x, y) sqrt(sum((x - y).^2));
    % case 'CityBlock'
    %     fun = @(x, y) sum(x-y) 
end`