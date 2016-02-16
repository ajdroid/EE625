clc;
load('../../data/power_line_interference_ecg.mat');
load('../../data/original_ECG.mat');
figure(1)
subplot(2,1,1)
plot(x_pl);
title('Noisy signal')
figure(2)
n = 100;
Yp=x_pl(500:500+n);
freqz(Yp);
title('Frequency response - powerline')
w0=.1; % central frequency
bandwidth=.1; % width of notch
[b,a] = iirnotch(w0,bandwidth); 
ecgplfilt = filter(b,a,x_pl);
figure(1)
subplot(2,1,2)
plot(ecgplfilt)
title('Filtered signal')
PRDpl = sqrt(sum((ecgplfilt - original).^2)/sum(original.^2))*100;

load('../../data/base_line_wandering_ecg.mat')
x_bs = baseline_noise_ecg;
figure(3)
subplot(2,1,1)
plot(x_bs);
title('Noisy signal')

figure(4)
Yb = x_bs;
freqz(Yb);
title('Frequency response - baseline wandering')

fth = 0.00325;
[b,a] = butter(2, fth, 'high');
ecgbsfilt = filter(b, a, baseline_noise_ecg);
PRDbs = sqrt(sum((ecgbsfilt - original).^2)/sum(original.^2))*100

figure(3)
subplot(2,1,2)
plot(ecgbsfilt)
title('Filtered signal')
