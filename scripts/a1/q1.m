clc;
clear all;
load('../../data/original_ECG.mat');

% Finding the R val
threshold = max(original)*0.95;
[pks,locs] = findpeaks(original, 'MinPeakHeight', threshold);

% Time between between R peaks
rDiff = diff(locs);
indices = locs(2:8);

% Heart rate signal
figure(1)

subplot(2,1,1);
plot(original);hold on;
plot(indices, rDiff, 'rv');
ylabel('Amplitude / heart rate');
xlabel('Time');
title('Original ECG signal');

subplot(2,1,2);
plot(indices, rDiff, 'rv');
xlabel('Time');
title('heart rate signal');

% mean and std deviation of R interval
average = mean(rDiff);
stdDeviation = std(rDiff);
