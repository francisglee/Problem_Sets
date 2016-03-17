function run_QDE()
clc; close all;

% species parameters 
speciesNames = {'X','Y','Z'};
tau = [1 1 1];
ymax = [1 1 1];
params = {tau,ymax};

% Initial conditions, ODE settings, and ODE simulation
y0 = [0 0 0];
tspan = [0 20]; 
options = []; 
[t,y] = ode15s(@ODEfun_coherentType1_FFL,tspan,y0,options,params);

% Plot results
figure; 
plot(t,y,'LineWidth',2); 
set(gca,'FontSize',14);
xlabel('Time'); ylabel('Fractional Species Activation'); 
legend(speciesNames);
title('Coherent type 1 FFL')
ylim([-.1 1.1])

%% ODE functions %%
function dydt = ODEfun_coherentType1_FFL(t,y,params)
[tau,ymax] = params{:};
% Assign species numeric values for easier handling
X = 1;
Y = 2;
Z = 3;

% Initialize output dydt vector - must be column vector
dydt = zeros(length(y),1);

% stimulus settings
stim = 1;
if t>=10; stim = 0; end

% reaction parameters
parXtoY = [1 3 0.5];
parXtoZ = [1 3 0.5];
parYtoZ = [1 3 0.5];

% ODEs - coherent type 1
dydt(X) = (stim*ymax(X)-y(X))/tau(X);
dydt(Y) = (act(y(X),parXtoY)*ymax(Y)-y(Y))/tau(Y);
dydt(Z) = (AND(act(y(X),parXtoZ),act(y(Y),parYtoZ))*ymax(Z)-y(Z))/tau(Z);

%% utility functions 
function fact = act(x,rpar) 
% hill activation function with parameters w (weight), n (Hill coeff), EC50 
    w = rpar(1);
    n = rpar(2);
    EC50 = rpar(3);
    if n == 1 && EC50 == 0.5
        beta = 1e5;
    else
        beta = (EC50.^n - 1)./(2*EC50.^n - 1);   
    end

    K = (beta - 1).^(1./n);
    fact = w.*(beta.*x.^n)./(K.^n + x.^n);
    if fact>1,                 % cap fact(x)<= 1 
        fact = 1; 
    end
 
function finhib = inhib(x,rpar) 
% inverse hill function with parameters w (weight), n (Hill coeff), EC50 
    finhib = 1 - act(x,rpar);
 
function z = OR(x,y) 
% OR logic gate 
    z = x + y - x*y;
 
function z = AND(varargin) 
% AND logic gate, multiplying all of the reactants together 
    z=prod(cell2mat(varargin));