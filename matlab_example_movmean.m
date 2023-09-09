% Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12];

% Define the window size for the moving average
window_size = 5

% Calculate the moving average
moving_average = movmean(data, window_size);

% Display the result
disp(moving_average);
