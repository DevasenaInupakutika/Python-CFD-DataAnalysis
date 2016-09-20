clc;
format long;
LL=3.0;
zz=151;      % no. of mesh points in vertical direction(z)
xx=801;     % no. of mesh points in x direction
dx=LL/(xx-1); % mesh size in x direction
n=1;
dn=1;
p=0;
disp('Sorting Data ...');
for p=1:320
m=n;
fname=['data.',num2str(m),'.csv']

%Loading Data File and skipping first Header line

fid  = fopen (fname);
data = textscan(fid,'%f%f%f%f%f%f%f%f','Delimiter',',','HeaderLines',1);
fid = fclose(fid);

% Creating the matrix which need to be sorted

data2=[data{1} data{3} data{4} data{6} data{7}];
x=0.0;

% Start Sorting

for j=1:xx   % cell no. in x direction

    a=find(abs((data2(:,4)-x))<0.0001);
 
    k1=(data2(a,1));    % Density array
    k2=(data2(a,2));    % velocity (Ux) array
    k3=(data2(a,3));    % velocity (Uy) array 
    k4=(data2(a,4));    % x coordinate array
    k5=(data2(a,5));    % z coordinate array
    
    % Sorted Matrix 
    mat=[k1,k2,k3,k4,k5];     %[density x y]
    x=x+dx;

% Compiling all the small matrices in final matrix

   from=(j-1)*zz+1;
   to=from+zz-1;
   F(from:to,:)=mat;

end
n=n+dn;
Final_matrix=F;
filename = ['Final', num2str(p), '.dat'];
dlmwrite(filename,Final_matrix,'precision','%.5f')
end
F;

% dlmwrite ('FMat.txt', F)
