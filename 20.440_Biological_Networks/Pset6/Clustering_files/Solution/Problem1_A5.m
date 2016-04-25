% define inputs
X = [0 2; 0 1; 1 2; 2.5 5; 3.1 5; 3.1 6; 4 2; 5 2; 5 0];
equation = distance('Euclidean');
equation2 = distance('CityBlock');
disp(equation);
krange = 3;
kset = [2 3 4];

% define starting dataset
dataset_euclidean = cell(krange, 1); % define dataset that will be used to evaluate MSE
dataset_cityblock = cell(krange, 1); % define dataset that will be used to evaluate MSE

% lets run kmeans cluster using 3 different k's for euclidean distance
for krange = 1:3
    for iteration = 1: 5 % run each k-value 5 times
        
        % to plot MSE vs k, we'll need only dist2centroids
        [c, centroids_list, dists2centroids] = kmeans_cluster(X, kset(krange), equation);
        dataset_euclidean{krange} = [dataset_euclidean{krange} dists2centroids]; % append each iteration to k location in dataset
        end
end


% lets run kmeans cluster using 3 different k's for cityblock distance
for krange = 1:3
    for iteration = 1: 5 % run each k-value 5 times
        
    % to plot MSE vs k, we'll need only dist2centroids
    [c, centroids_list, dists2centroids] = kmeans_cluster(X, kset(krange), equation2);
    dataset_cityblock{krange} = [dataset_cityblock{krange} dists2centroids]; % append each iteration to k location in dataset
    end
end

%{
disp(dataset_euclidean);
disp(dataset_cityblock);
%}

% To plot MSE, we'll need to take the mean of distance squared
% define MSE dataset
mse_euclidean = cell(krange, 1); 
mse_cityblock = cell(krange, 1); 

% populate mse_euclidean
for cell = dataset_euclidean
    tally = 0; % define tally
    for item = cell
        tally = tally + (item * item);
    mse_euclidean{cell} = sqrt(tally);
    end
end

% populate mse_cityblock
for cell = dataset_cityblock
    tally = 0; % define tally
    for item = cell
        tally = tally + (item * item);
    mse_cityblock{cell} = sqrt(tally);
    end
end

disp(mse_euclidean);
disp(mse_cityblock);

