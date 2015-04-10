function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

TD =  [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
pre_err = zeros(length(TD));
for i = 1:length(TD)
    for j = 1:length(TD)
        C = TD(i);
        sigma = TD(j);
        model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
        predictions = svmPredict(model, Xval);
        pre_err(i, j) = mean(double(predictions ~= yval));
    end
end
mm = min(min(pre_err));
[ind_C, ind_sigma] = find(pre_err == mm);
C = TD(ind_C);
sigma = TD(ind_sigma);

% =========================================================================

end
