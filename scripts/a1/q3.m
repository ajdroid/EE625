clc;
safety = audioread('safety.wav');

figure(1)
plot(safety);
title('Safety speech signal');

windowSize = 400;
sizeSignal = size(safety);
n = floor(sizeSignal(1)/windowSize);
zeroCrossings = zeros(n,1);
energy = zeros(n,1);

for i = 0:n-1
    temp = safety(windowSize*i+1:windowSize+windowSize*i);
    for j = 1:windowSize
        if temp(j,1) ==  0
            zeroCrossings(i+1) = zeroCrossings(i+1)+1;
        end
        energy(i+1,1) = energy(i+1,1)+temp(j,1)^2;
    end
    if (energy(i+1,1)>1 && zeroCrossings(i+1,1)<100)
        voiced(windowSize*i+1:windowSize+windowSize*i) = safety(windowSize*i+1:windowSize+windowSize*i);
        figure(2);
        subplot(2,1,1);
        plot(voiced);
        title('Voiced regions');
    elseif (energy(i+1,1)>.09 && energy(i+1,1)<1 && zeroCrossings(i+1,1)<150)
        unVoiced(windowSize*i+1:windowSize+windowSize*i) = safety(windowSize*i+1:windowSize+windowSize*i);
        figure(2);
        subplot(2,1,2);
        plot(unVoiced);
        title('Unvoiced regions');
    end
    if (energy(i+1,1)<.05 )
        nonSpeech(windowSize*i+1:windowSize+windowSize*i) = safety(windowSize*i+1:windowSize+windowSize*i);
        figure(3);
        subplot(2,1,1);
        plot(nonSpeech);
        title('Non-Speech regions');
    else
        speech(windowSize*i+1:windowSize+windowSize*i) = safety(windowSize*i+1:windowSize+windowSize*i);
        figure(3);
        subplot(2,1,2);
        plot(speech);
        title('Speech regions');
    end
end