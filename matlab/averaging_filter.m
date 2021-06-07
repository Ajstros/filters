% We want to average the incoming data with the last data point
% Ex. Input: 0, 0, 0, 0, 1023, 1023, 1023, 1023
%    Output:    0, 0, 0, 512,  1023, 1023, 1023

%%
input = [0, 0, 0, 0, 1023, 1023, 1023, 1023];
output = zeros(8, 1);
moving_average = dsp.MovingAverage(2);
for i = 1:8
    output(i) = moving_average(input(i)); % Expecting [0, 0, 0, 512,  1023, 1023, 1023]
end

output