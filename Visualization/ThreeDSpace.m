%To initialize a 3D space
%{
ax = axes();
xlim(ax, [-20 20]);
ylim(ax, [-20 20]);
zlim(ax, [-20 20]);
view(ax, 3)
hold(ax, 'on')
point1 = [1 2 3];
%}

%Random Data
x = (1:.01:2*pi)';
y = sin(x);
z = 4*x;
%Animated Figure
figure;
hold on;
%plot3(x(1),y(1),z(1),'db');
hPlot = plot3(x(1), y(1), z(1), 'db');
view(3);
axis([min(x) max(x) min(y) max(y) min(z) max(z)]);
xlabel('X', 'Interpreter','Latex');
ylabel('Y', 'Interpreter','Latex');
zlabel('Z', 'Interpreter', 'Latex');
grid on;
box on;
for k = 2:length(x) %loop
    set(hPlot, 'XData', x(k), 'YData', y(k), 'ZData', z(k));
    drawnow;
end
hold off;