function problem1B_kmeans()

%% K-means clustering funtion
function [c,centroids,dists2centroids] = kmeans_cluster(X,k,distFun)
% Cutoff criteria 
epsilon = 1e-7; % Some small value

% Initialize cutoff values
maxEpsilon = 100; % Set to some large value initially

% Get intiial centroids by randomly sampling input matrix
% Assumes clustering dimension is by rows
rand_vals = randperm(size(X, 1));
centroids = X(rand_vals(1:k), : ); 

% Begin loop and continue until cutoffs met
while maxEpsilon > epsilon

    % Determine distances to current centroids DONE

    % Get membership of observations to clusters based on distance DONE
    
    % Re-calculate centroids based on current assignments DONE
 
    % Compute change in centroids DONE
    
    % Update centroids to new ones
    
    % update epsilon cutoff value
    
end

% Assign final membership, centroids, and distances to centroids

%% Distance function
function fun = distance(dist)
switch dist
    case 'Euclidean'
        fun = @(x, y) sqrt(sum((x - y).^2));
    case 'CityBlock'
        fun = @(x, y) sum(abs(x - y)); 
end