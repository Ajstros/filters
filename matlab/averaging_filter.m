% We want to average the incoming data with the last data point
% Ex. Input: 0, 0, 0, 0, 1023, 1023, 1023, 1023
%    Output:    0, 0, 0, 512,  1023, 1023, 1023

%%
input = [10, 0, 0, 0, 1023, 1023, 1023, 1023];
moving_average = dsp.MovingAverage('WindowLength', 8);
output = moving_average(input) % Expecting [0, 0, 0, 512,  1023, 1023, 1023]

%%
x = [1, 2, 3, 4, 5, 6, 7, 8, 9];
moving_average = dsp.MovingAverage(2);
y = moving_average(x)