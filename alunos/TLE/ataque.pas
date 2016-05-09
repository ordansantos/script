var
  n,i,x,y,s:longint;
  a,b:array[-1000..2000]of longint;
begin
	for i:=1 to 1000000000 do
		writeln('aa');
  read(n);
  for i:=1 to n do
    begin
      read(x,y);
      a[x+y]:=a[x+y]+1;
      b[x+y]:=b[x+y]+1;
    end;
  for i:=-1000 to 2000 do
    s:=s+a[i]*(a[i]-1) div 2+b[i]*(b[i]-1) div 2;
  writeln(s);
end.
