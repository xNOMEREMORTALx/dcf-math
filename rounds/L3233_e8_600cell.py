import numpy as np, itertools
phi=(1+5**.5)/2
# --- E8 roots
R=[]
for i,j in itertools.combinations(range(8),2):
    for si in (1,-1):
        for sj in (1,-1):
            v=np.zeros(8); v[i]=si; v[j]=sj; R.append(v)
for signs in itertools.product((0.5,-0.5),repeat=8):
    if sum(s<0 for s in signs)%2==0: R.append(np.array(signs))
R=np.array(R); G=R@R.T
print("E8: roots",len(R),"| norm^2 values",sorted(set(np.round(np.diag(G),6))),"| neighbours at inner product 1:",set((np.isclose(G,1)).sum(1)))
print("E8 packing density pi^4/384 =",np.pi**4/384)
# --- 600-cell (unit quaternions, binary icosahedral group)
V=[]
for i in range(4):
    for s in (1,-1): v=np.zeros(4); v[i]=s; V.append(v)
for s in itertools.product((0.5,-0.5),repeat=4): V.append(np.array(s))
base=[phi/2,0.5,1/(2*phi),0]
evens=[p for p in itertools.permutations(range(4)) if sum(1 for a in range(4) for b in range(a+1,4) if p[a]>p[b])%2==0]
for p in evens:
    for s in itertools.product((1,-1),repeat=3):
        v=np.zeros(4); vals=[base[0]*s[0],base[1]*s[1],base[2]*s[2],0]
        for k in range(4): v[p[k]]=vals[k]
        V.append(v)
V=np.unique(np.round(np.array(V),9),axis=0)
D=np.linalg.norm(V[:,None]-V[None],axis=2); e=np.min(D[D>1e-9])
nbr=(np.isclose(D,e)).sum(1); edges=int(np.isclose(D,e).sum()/2)
A=np.isclose(D,e)
tri=sum(1 for i in range(len(V)) for j in np.where(A[i])[0] if j>i for k in np.where(A[i]&A[j])[0] if k>j)
tet=0
for i in range(len(V)):
    for j in np.where(A[i])[0]:
        if j<=i: continue
        c=np.where(A[i]&A[j])[0]
        for k in c:
            if k<=j: continue
            tet+=sum(1 for l in c if l>k and A[k,l])
print("600-cell: vertices",len(V),"| edge length %.6f (1/phi = %.6f)"%(e,1/phi),"| neighbours per vertex",set(nbr),"| edges",edges,"| triangles",tri,"| tetrahedral cells",tet)
# --- E8 -> 4D via the Coxeter element (h = 30)
simple=[np.array([1,-1,0,0,0,0,0,0.]),np.array([0,1,-1,0,0,0,0,0.]),np.array([0,0,1,-1,0,0,0,0.]),np.array([0,0,0,1,-1,0,0,0.]),
        np.array([0,0,0,0,1,-1,0,0.]),np.array([0,0,0,0,0,1,-1,0.]),np.array([0,0,0,0,0,1,1,0.]),np.array([-.5]*8)]
def refl(a): return np.eye(8)-2*np.outer(a,a)/(a@a)
C=np.eye(8)
for a in simple: C=C@refl(a)
w,U=np.linalg.eig(C); ang=np.round(np.angle(w)*30/(2*np.pi)).astype(int)%30
print("Coxeter element order check: C^30 = I?",np.allclose(np.linalg.matrix_power(C,30),np.eye(8)),"| exponents",sorted(ang))
def plane(m):
    k=[i for i in range(8) if ang[i]==m][0]; return np.real(U[:,k]),np.imag(U[:,k])
B=np.array([*plane(1),*plane(11)]); Q,_=np.linalg.qr(B.T); P=R@Q
n=np.linalg.norm(P,axis=1); vals=np.unique(np.round(n,6))
print("E8 roots projected to the (1,11) Coxeter 4-space: distinct radii",vals,"counts",[int(np.isclose(n,v).sum()) for v in vals],"ratio %.6f (phi %.6f)"%(vals[-1]/vals[0],phi))
for v in vals:
    S=P[np.isclose(n,v)]/v; d=np.linalg.norm(S[:,None]-S[None],axis=2); m=np.min(d[d>1e-9])
    print("  shell r=%.4f: points %d, nearest-neighbour count per point %s, nn distance %.4f (600-cell: 12 at 1/phi=%.4f)"%(v,len(S),set(np.isclose(d,m).sum(1)),m,1/phi))
