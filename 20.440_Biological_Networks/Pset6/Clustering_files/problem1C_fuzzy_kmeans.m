function problem1C_fuzzy_kmeans()

%% Fuzzy K-means clustering function
function [U,centroids,dists2centroids] = fuzzy_kmeans(X,k,fuzzifier,distFun)
% Cutoff criteria 
epsilon = 1e-3;

% Initialize cutoff values
maxEpsilon = 100;

% Get intiial centroids
rand_vals = randperm(size(X,1));
centroids = X(rand_vals(1:k),:)+randn(size(X(rand_vals(1:k),:)));

% Begin loop and continue until cutoffs met
m = fuzzifier; 
N = size(X,1);
U = zeros(N,k);
while maxEpsilon > epsilon

    % Determine distances to centroids and create U (membership) matrix
    
    % Update centroids based on current assignment
   
    % Compute change in centroids
    
    % Update centroids to new ones
    
    % update cutoff values
    
end

% Assign final membership, centroids, and distances to centroids

function fun = distance(dist)
switch dist
    case 'Euclidean'
        fun = @(x,y) sqrt(sum((x-y).^2));
end