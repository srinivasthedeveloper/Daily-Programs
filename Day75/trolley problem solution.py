#JAVA SCRIPT SOLUTION:-
t=[]
const N = parseInt(readline()); // The numbers of paths the train can take
for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    const Q = parseInt(inputs[0]); // The number of persons on the path
    const V = parseInt(inputs[1]); // The individual value of each person on the path
    t.push(Q*V)
}

t=t.map(x=>parseInt(x))

console.log(t.indexOf(Math.min(...t))+1);


#Python Solution

l=[[eval("*".join(input().split()))]for i in range(int(input()))]
print(l.index(min(l))+1)