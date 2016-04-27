
%% Distance function
function fun = distance(dist)
switch dist
    case 'Euclidean'
        fun = @(x, y) sqrt(sum((x - y).^2));
    case 'CityBlock'
        fun = @(x, y) sum(abs(x - y)); 
end

